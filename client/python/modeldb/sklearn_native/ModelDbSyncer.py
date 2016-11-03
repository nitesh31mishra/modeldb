"""
This is the Syncer that is responsible for storing events in the ModelDB.
Contains functions for overriding basic scikit-learn functions.
"""
import sys
import numpy as np
import pandas as pd

# sklearn imports
from sklearn.linear_model import *
from sklearn.preprocessing import *
from sklearn.decomposition import *
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
import sklearn.metrics

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

# modeldb imports
import GridCrossValidation
from ..basic import *
from ..events import *
from ..thrift.modeldb import ModelDBService
from ..thrift.modeldb import ttypes as modeldb_types



def fit_fn(self, x, y=None, sample_weight=None):
    """
    Overrides the fit function for all models except for Pipeline and GridSearch
    Cross Validation, which have their own functions.
    """
    df = x
    #Certain fit functions only accept one argument
    if y is None:
        models = self.fit(x)
    else:
        models = self.fit(x, y)
        yDf = pd.DataFrame(y)
        if type(x) is pd.DataFrame:
            df = x.join(yDf)
        else:
            #if x does not have column-names, we cannot perform a join, and
            #must instead add a new column.
            df = pd.DataFrame(x)
            df['outputColumn'] = y
    #Calls FitEvent in other class and adds to buffer
    fit_event = FitEvent(models, self, df)
    if hasattr(x, 'tag') and x.tag != "":
        add_tag_object(df, x.tag)
    Syncer.instance.add_to_buffer(fit_event)

def predict_fn(self, x):
    """
    Overrides the predict function for models, provided that the predict
    function takes in one argument.
    """
    predict_array = self.predict(x)
    predict_df = pd.DataFrame(predict_array)
    new_df = x.join(predict_df)
    predict_event = TransformEvent(x, new_df, self)
    Syncer.instance.add_to_buffer(predict_event)
    return predict_array

def transform_fn(self, x):
    """
    Overrides the transform function for models, provided that the
    transform function takes in one argument.
    """
    transformed_output = self.transform(x)
    if type(transformed_output) is np.ndarray:
        new_df = pd.DataFrame(transformed_output)
    else:
        new_df = pd.DataFrame(transformed_output.toarray())
    transform_event = TransformEvent(x, new_df, self)
    Syncer.instance.add_to_buffer(transform_event)
    return transformed_output

def fit_fn_pipeline(self, x, y):
    """
    Overrides the Pipeline model's fit function
    """
    #Check if pipeline contains valid estimators and transformers
    check_valid_pipeline(self.steps)

    #Make Fit Event for overall pipeline
    pipeline_model = self.fit(x, y)
    pipeline_fit = FitEvent(pipeline_model, self, x)

    #Extract all the estimators from pipeline
    #All estimators call 'fit' and 'transform' except the last estimator (which only calls 'fit')
    names, sk_estimators = zip(*self.steps)
    estimators = sk_estimators[:-1]
    last_estimator = sk_estimators[-1]

    transform_stages = []
    fit_stages = []
    cur_dataset = x

    for index, estimator in enumerate(estimators):
        old_df = cur_dataset
        model = estimator.fit(old_df, y)
        transformed_output = model.transform(old_df)

        #Convert transformed output into a proper pandas DataFrame object
        if type(transformed_output) is np.ndarray:
            new_df = pd.DataFrame(transformed_output)
        else:
            new_df = pd.DataFrame(transformed_output.toarray())

        cur_dataset = transformed_output

        #populate the stages
        transform_event = TransformEvent(old_df, new_df, model)
        transform_stages.append((index, transform_event))
        fit_event = FitEvent(model, estimator, old_df)
        fit_stages.append((index, fit_event))

    #Handle last estimator, which has a fit method (and may not have transform)
    old_df = cur_dataset
    model = last_estimator.fit(old_df, y)
    fit_event = FitEvent(model, last_estimator, old_df)
    fit_stages.append((index+1, fit_event))

    #Create the pipeline event with all components
    pipeline_event = PipelineEvent(pipeline_fit, transform_stages, fit_stages)

    Syncer.instance.add_to_buffer(pipeline_event)

def check_valid_pipeline(steps):
    """
    Helper function to check whether a pipeline is constructed properly. Taken
    from original sklearn pipeline source code with minor modifications,
    which are commented below.
    """
    names, estimators = zip(*steps)
    transforms = estimators[:-1]
    estimator = estimators[-1]

    for t in transforms:
        #Change from original scikit: checking for "fit" and "transform"
        #methods, rather than "fit_transform" as each event is logged separately to database
        if not (hasattr(t, "fit")) and hasattr(t, "transform"):
            raise TypeError("All intermediate steps of the chain should "
                            "be transforms and implement fit and transform"
                            " '%s' (type %s) doesn't)" % (t, type(t)))

    if not hasattr(estimator, "fit"):
        raise TypeError("Last step of chain should implement fit "
                        "'%s' (type %s) doesn't)"
                        % (estimator, type(estimator)))

def fit_fn_grid_search(self, x, y):
    """
    Overrides GridSearch Cross Validation's fit function
    """
    GridCrossValidation.fit(self, x, y)
    [input_data_frame, cross_validations, seed, evaluator, best_model,
        best_estimator, num_folds] = self.grid_cv_event

    #Calls SyncGridCVEvent and adds to buffer.
    grid_event = GridSearchCVEvent(input_data_frame, cross_validations,
        seed, evaluator, best_model, best_estimator, num_folds)
    Syncer.instance.add_to_buffer(grid_event)

def add_tag_object(self, tag_name):
    """
    Stores object with associated tagName
    """
    if type(tag_name) is str:
        self.tag = tag_name
        Syncer.instance.store_tag_object(id(self), tag_name)

def store_df_path(filepath_or_buffer, **kwargs):
    """
    Stores the filepath for a dataframe
    """
    df = pd.read_csv(filepath_or_buffer, **kwargs)
    Syncer.instance.path_for_df[id(df)] = filepath_or_buffer
    return df

class Syncer(ModelDbSyncerBase.Syncer):
    """
    This is the Syncer class for sklearn functionality, responsible for
    storing events in the ModelDB.
    """
    def __init__(self, project_config, experiment_config, experiment_run_config):
        super(Syncer, self).__init__(project_config, experiment_config, experiment_run_config)
        self.id_for_object = {}
        self.object_for_id = {}
        self.tag_for_object = {}
        self.object_for_tag = {}
        self.path_for_df = {}
        self.enable_sync_functions()
        self.add_tags()
        self.add_dataframe_path()

    def __str__(self):
        return "SklearnSyncer"

    def store_object(self, obj, Id):
        """
        Stores mapping between objects and their IDs.
        """
        self.id_for_object[obj] = Id
        self.object_for_id[Id] = obj

    def store_tag_object(self, obj, tag):
        """
        Stores mapping between objects and their tags.
        Tags are short, user-generated names.
        """
        self.tag_for_object[obj] = tag
        self.object_for_tag[tag] = obj

    def add_to_buffer(self, event):
        """
        As events are generated, they are added to this buffer.
        """
        self.buffer_list.append(event)

    def sync(self):
        """
        When this function is called, all events in the buffer are stored on server.
        """
        for b in self.buffer_list:
            b.sync(self)
        self.clear_buffer()

    def set_columns(self, df):
        """
        Helper function to extract column names from a dataframe.
        Pandas dataframe objects are treated differently from
        numpy arrays.
        """
        if type(df) is pd.DataFrame:
            columns = df.columns.values
            if type(columns) is np.ndarray:
                columns = np.array(columns).tolist()
            for i in range(0, len(columns)):
                columns[i] = str(columns[i])
        else:
            columns = []
        return columns

    def setDataFrameSchema(self, df):
        """
        Helper function designated to extract the column schema
        within a dataframe.
        """
        data_frame_cols = []
        columns = self.set_columns(df)
        for i in range(0, len(columns)):
            columnName = str(columns[i])
            dfc = modeldb_types.DataFrameColumn(columnName, str(df.dtypes[i]))
            data_frame_cols.append(dfc)
        return data_frame_cols

    def convert_model_to_thrift(self, model):
        """
        Converts a model into a Thrift object with appropriate fields.
        """
        tid = -1
        tag = ""
        if model in self.id_for_object:
            tid = self.id_for_object[model]
        if id(model) in self.tag_for_object:
            tag = self.tag_for_object[id(model)]
        transformer_type = model.__class__.__name__
        t = modeldb_types.Transformer(tid, transformer_type, tag)
        return t

    def convert_df_to_thrift(self, df):
        """
        Converts a dataframe into a Thrift object with appropriate fields.
        """
        tid = -1
        tag = ""
        filepath = ""
        dfImm = id(df)
        if dfImm in self.id_for_object:
            tid = self.id_for_object[dfImm]
        if dfImm in self.tag_for_object:
            tag = self.tag_for_object[dfImm]
        dataframe_columns = self.setDataFrameSchema(df)
        if dfImm in self.path_for_df:
            filepath = self.path_for_df[dfImm]
        modeldb_df = modeldb_types.DataFrame(
            tid, dataframe_columns, df.shape[0], tag, filepath)
        return modeldb_df

    def convert_spec_to_thrift(self, spec):
        """
        Converts a TransformerSpec object into a Thrift object with appropriate fields.
        """
        tid = -1
        tag = ""
        if spec in self.id_for_object:
            tid = self.id_for_object[spec]
        if id(spec) in self.tag_for_object:
            tag = self.tag_for_object[id(spec)]
        hyperparams = []
        params = spec.get_params()
        for param in params:
            hp = modeldb_types.HyperParameter(
                param, 
                str(params[param]),
                type(params[param]).__name__,
                sys.float_info.min, 
                sys.float_info.max)
            hyperparams.append(hp)
        ts = modeldb_types.TransformerSpec(tid, spec.__class__.__name__, 
            hyperparams, tag)
        return ts

    def add_tags(self):
        """
        Adds tag as a method to objects, allowing users to tag objects with their own description
        """
        setattr(pd.DataFrame, "tag", add_tag_object)
        models = [LogisticRegression, LinearRegression, LabelEncoder, 
            OneHotEncoder, Pipeline, GridSearchCV, PCA]
        for class_name in models:
            setattr(class_name, "tag", add_tag_object)

    def add_dataframe_path(self):
        """
        Adds the read_csv_sync function, allowing users to automatically track dataframe location
        """
        setattr(pd, "read_csv_sync", store_df_path)

    def enable_sync_functions(self):
        """
        This function extends the scikit classes to implement custom
        *Sync versions of methods. (i.e. fit_sync() for fit())
        Users can easily add more models to this function.
        """
        #Linear Models (transform has been deprecated)
        for class_name in [LogisticRegression, LinearRegression]:
            setattr(class_name, "fit_sync", fit_fn)
            setattr(class_name, "predict_sync", predict_fn)

        #Preprocessing models
        for class_name in [LabelEncoder, OneHotEncoder]:
            setattr(class_name, "fit_sync", fit_fn)
            setattr(class_name, "transform_sync", transform_fn)

        #Pipeline model
        for class_name in [Pipeline]:
            setattr(class_name, "fit_sync", fit_fn_pipeline)

        #Grid-Search Cross Validation model
        for class_name in [GridSearchCV]:
            setattr(class_name, "fit_sync", fit_fn_grid_search)
