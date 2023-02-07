# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: monitoring/Alert.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ..common import CommonService_pb2 as common_dot_CommonService__pb2
from ..monitoring import MonitoredEntity_pb2 as monitoring_dot_MonitoredEntity__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16monitoring/Alert.proto\x12\x13\x61i.verta.monitoring\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1a\x63ommon/CommonService.proto\x1a monitoring/MonitoredEntity.proto\"P\n\x1bNotificationChannelTypeEnum\"1\n\x17NotificationChannelType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05SLACK\x10\x01\"\xad\x02\n\x13NotificationChannel\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x11\x63reated_at_millis\x18\x03 \x01(\x04\x12\x19\n\x11updated_at_millis\x18\x04 \x01(\x04\x12V\n\x04type\x18\x05 \x01(\x0e\x32H.ai.verta.monitoring.NotificationChannelTypeEnum.NotificationChannelType\x12M\n\rslack_webhook\x18\x06 \x01(\x0b\x32\x34.ai.verta.monitoring.NotificationChannelSlackWebhookH\x00\x12\x14\n\x0cworkspace_id\x18\x07 \x01(\x04\x42\t\n\x07\x63hannel\".\n\x1fNotificationChannelSlackWebhook\x12\x0b\n\x03url\x18\x01 \x01(\t\"\xaa\x03\n CreateNotificationChannelRequest\x12\x39\n\x07\x63hannel\x18\x01 \x01(\x0b\x32(.ai.verta.monitoring.NotificationChannel\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x11\x63reated_at_millis\x18\x03 \x01(\x04\x12\x19\n\x11updated_at_millis\x18\x04 \x01(\x04\x12\x16\n\x0cworkspace_id\x18\x07 \x01(\x04H\x00\x12\x18\n\x0eworkspace_name\x18\x08 \x01(\tH\x00\x12V\n\x04type\x18\x05 \x01(\x0e\x32H.ai.verta.monitoring.NotificationChannelTypeEnum.NotificationChannelType\x12M\n\rslack_webhook\x18\x06 \x01(\x0b\x32\x34.ai.verta.monitoring.NotificationChannelSlackWebhookH\x01\x42\x16\n\x14workspace_identifierB\x16\n\x14notification_channel\"]\n UpdateNotificationChannelRequest\x12\x39\n\x07\x63hannel\x18\x01 \x01(\x0b\x32(.ai.verta.monitoring.NotificationChannel\"\xcf\x02\n\x1e\x46indNotificationChannelRequest\x12\x0b\n\x03ids\x18\x01 \x03(\x04\x12\r\n\x05names\x18\x02 \x03(\t\x12?\n\x05types\x18\x03 \x03(\x0b\x32\x30.ai.verta.monitoring.NotificationChannelTypeEnum\x12\x13\n\x0bpage_number\x18\x04 \x01(\x05\x12\x12\n\npage_limit\x18\x05 \x01(\x05\x12\x16\n\x0cworkspace_id\x18\x06 \x01(\x04H\x00\x12\x18\n\x0eworkspace_name\x18\x07 \x01(\tH\x00\x1a]\n\x08Response\x12:\n\x08\x63hannels\x18\x01 \x03(\x0b\x32(.ai.verta.monitoring.NotificationChannel\x12\x15\n\rtotal_records\x18\x02 \x01(\x05\x42\x16\n\x14workspace_identifier\"/\n DeleteNotificationChannelRequest\x12\x0b\n\x03ids\x18\x01 \x03(\x04\"R\n\x0f\x41lerterTypeEnum\"?\n\x0b\x41lerterType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05\x46IXED\x10\x01\x12\r\n\tREFERENCE\x10\x02\x12\t\n\x05RANGE\x10\x03\"Z\n\x0f\x41lertStatusEnum\"G\n\x0b\x41lertStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x0c\n\x08\x41LERTING\x10\x02\x12\t\n\x05PAUSE\x10\x03\x12\n\n\x06NODATA\x10\x04\"b\n\x17\x45valuationFrequencyEnum\"G\n\x13\x45valuationFrequency\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x10\n\x0c\x46IVE_MINUTES\x10\x01\x12\x08\n\x04HOUR\x10\x02\x12\x07\n\x03\x44\x41Y\x10\x03\"^\n\x15\x41ggregationWindowEnum\"E\n\x11\x41ggregationWindow\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x10\n\x0c\x46IVE_MINUTES\x10\x01\x12\x08\n\x04HOUR\x10\x02\x12\x07\n\x03\x44\x41Y\x10\x03\"\xac\x07\n\x05\x41lert\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1b\n\x13monitored_entity_id\x18\x03 \x01(\x04\x12\x19\n\x11\x63reated_at_millis\x18\x04 \x01(\x04\x12\x19\n\x11updated_at_millis\x18\x05 \x01(\x04\x12 \n\x18last_evaluated_at_millis\x18\x06 \x01(\x04\x12S\n\x15notification_channels\x18\x07 \x03(\x0b\x32\x34.ai.verta.monitoring.Alert.NotificationChannelsEntry\x12@\n\x06status\x18\t \x01(\x0e\x32\x30.ai.verta.monitoring.AlertStatusEnum.AlertStatus\x12\x46\n\x0c\x61lerter_type\x18\x0b \x01(\x0e\x32\x30.ai.verta.monitoring.AlerterTypeEnum.AlerterType\x12\x38\n\ralerter_fixed\x18\x0c \x01(\x0b\x32\x1f.ai.verta.monitoring.AlertFixedH\x00\x12@\n\x11\x61lerter_reference\x18\r \x01(\x0b\x32#.ai.verta.monitoring.AlertReferenceH\x00\x12\x38\n\ralerter_range\x18\x0e \x01(\x0b\x32\x1f.ai.verta.monitoring.AlertRangeH\x00\x12\x16\n\x0eversion_number\x18\x0f \x01(\x04\x12\x0f\n\x07\x66\x65\x61ture\x18\x10 \x01(\t\x12X\n\x12\x61ggregation_window\x18\x12 \x01(\x0e\x32<.ai.verta.monitoring.AggregationWindowEnum.AggregationWindow\x12^\n\x14\x65valuation_frequency\x18\x13 \x01(\x0e\x32@.ai.verta.monitoring.EvaluationFrequencyEnum.EvaluationFrequency\x12\x18\n\x10\x61ggregation_type\x18\x14 \x01(\t\x12\x1d\n\x15\x61ggregation_algorithm\x18\x15 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x16 \x01(\x08\x1a;\n\x19NotificationChannelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x42\t\n\x07\x61lerterJ\x04\x08\x08\x10\tJ\x04\x08\n\x10\x0b\"Y\n\nAlertFixed\x12\x11\n\tthreshold\x18\x01 \x01(\x02\x12\x38\n\x08operator\x18\x02 \x01(\x0e\x32&.ai.verta.common.OperatorEnum.Operator\"V\n\nAlertRange\x12\x13\n\x0blower_bound\x18\x01 \x01(\x02\x12\x13\n\x0bupper_bound\x18\x02 \x01(\x02\x12\x1e\n\x16\x61lert_if_outside_range\x18\x03 \x01(\x08\"c\n\x0e\x41lertReference\x12\x11\n\tthreshold\x18\x01 \x01(\x02\x12\x38\n\x08operator\x18\x03 \x01(\x0e\x32&.ai.verta.common.OperatorEnum.OperatorJ\x04\x08\x02\x10\x03\"?\n\x12\x43reateAlertRequest\x12)\n\x05\x61lert\x18\x01 \x01(\x0b\x32\x1a.ai.verta.monitoring.Alert\"?\n\x12UpdateAlertRequest\x12)\n\x05\x61lert\x18\x02 \x01(\x0b\x32\x1a.ai.verta.monitoring.Alert\"\xa2\x03\n\x10\x46indAlertRequest\x12\x0b\n\x03ids\x18\x01 \x03(\x04\x12\r\n\x05names\x18\x02 \x03(\t\x12\x1c\n\x14monitored_entity_ids\x18\x03 \x03(\x04\x12&\n\x1elast_evaluated_at_millis_after\x18\x04 \x01(\x04\x12G\n\ralerter_types\x18\x05 \x03(\x0e\x32\x30.ai.verta.monitoring.AlerterTypeEnum.AlerterType\x12@\n\x06status\x18\x06 \x03(\x0e\x32\x30.ai.verta.monitoring.AlertStatusEnum.AlertStatus\x12\x17\n\x0fincludeIfNoData\x18\x0c \x01(\x08\x12\x13\n\x0bpage_number\x18\x07 \x01(\x05\x12\x12\n\npage_limit\x18\x08 \x01(\x05\x1aM\n\x08Response\x12*\n\x06\x61lerts\x18\x01 \x03(\x0b\x32\x1a.ai.verta.monitoring.Alert\x12\x15\n\rtotal_records\x18\x02 \x01(\x05J\x04\x08\t\x10\nJ\x04\x08\n\x10\x0bJ\x04\x08\x0b\x10\x0c\"!\n\x12\x44\x65leteAlertRequest\x12\x0b\n\x03ids\x18\x01 \x03(\x04\"\xa1\x01\n\x18UpdateAlertStatusRequest\x12\x10\n\x08\x61lert_id\x18\x01 \x01(\x04\x12\x19\n\x11\x65vent_time_millis\x18\x02 \x01(\x04\x12@\n\x06status\x18\x03 \x01(\x0e\x32\x30.ai.verta.monitoring.AlertStatusEnum.AlertStatusJ\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07J\x04\x08\x07\x10\x08\"m\n\x17ListAlertHistoryRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x1a\x46\n\x08Response\x12:\n\x07history\x18\x01 \x03(\x0b\x32).ai.verta.monitoring.ListAlertHistoryItem\"\xb6\x01\n\x14ListAlertHistoryItem\x12\x19\n\x11\x65vent_time_millis\x18\x01 \x01(\x04\x12@\n\x06status\x18\x02 \x01(\x0e\x32\x30.ai.verta.monitoring.AlertStatusEnum.AlertStatus\x12\x10\n\x08\x65vent_id\x18\x04 \x01(\t\x12)\n\x05\x61lert\x18\x05 \x01(\x0b\x32\x1a.ai.verta.monitoring.AlertJ\x04\x08\x03\x10\x04\x32\xfe\x0c\n\x0c\x41lertService\x12\xbc\x01\n\x19\x63reateNotificationChannel\x12\x35.ai.verta.monitoring.CreateNotificationChannelRequest\x1a(.ai.verta.monitoring.NotificationChannel\">\x82\xd3\xe4\x93\x02\x38\"3/api/v1/monitoring/alerts/createNotificationChannel:\x01*\x12\xbc\x01\n\x19updateNotificationChannel\x12\x35.ai.verta.monitoring.UpdateNotificationChannelRequest\x1a(.ai.verta.monitoring.NotificationChannel\">\x82\xd3\xe4\x93\x02\x38\"3/api/v1/monitoring/alerts/updateNotificationChannel:\x01*\x12\xca\x01\n\x17\x66indNotificationChannel\x12\x33.ai.verta.monitoring.FindNotificationChannelRequest\x1a<.ai.verta.monitoring.FindNotificationChannelRequest.Response\"<\x82\xd3\xe4\x93\x02\x36\"1/api/v1/monitoring/alerts/findNotificationChannel:\x01*\x12\xae\x01\n\x19\x64\x65leteNotificationChannel\x12\x35.ai.verta.monitoring.DeleteNotificationChannelRequest\x1a\x1a.ai.verta.monitoring.Empty\">\x82\xd3\xe4\x93\x02\x38*3/api/v1/monitoring/alerts/deleteNotificationChannel:\x01*\x12\x84\x01\n\x0b\x63reateAlert\x12\'.ai.verta.monitoring.CreateAlertRequest\x1a\x1a.ai.verta.monitoring.Alert\"0\x82\xd3\xe4\x93\x02*\"%/api/v1/monitoring/alerts/createAlert:\x01*\x12\x84\x01\n\x0bupdateAlert\x12\'.ai.verta.monitoring.UpdateAlertRequest\x1a\x1a.ai.verta.monitoring.Alert\"0\x82\xd3\xe4\x93\x02*\"%/api/v1/monitoring/alerts/updateAlert:\x01*\x12\x96\x01\n\x11updateAlertStatus\x12-.ai.verta.monitoring.UpdateAlertStatusRequest\x1a\x1a.ai.verta.monitoring.Empty\"6\x82\xd3\xe4\x93\x02\x30\"+/api/v1/monitoring/alerts/updateAlertStatus:\x01*\x12\x92\x01\n\tfindAlert\x12%.ai.verta.monitoring.FindAlertRequest\x1a..ai.verta.monitoring.FindAlertRequest.Response\".\x82\xd3\xe4\x93\x02(\"#/api/v1/monitoring/alerts/findAlert:\x01*\x12\xae\x01\n\x10listAlertHistory\x12,.ai.verta.monitoring.ListAlertHistoryRequest\x1a\x35.ai.verta.monitoring.ListAlertHistoryRequest.Response\"5\x82\xd3\xe4\x93\x02/\"*/api/v1/monitoring/alerts/listAlertHistory:\x01*\x12\x84\x01\n\x0b\x64\x65leteAlert\x12\'.ai.verta.monitoring.DeleteAlertRequest\x1a\x1a.ai.verta.monitoring.Empty\"0\x82\xd3\xe4\x93\x02**%/api/v1/monitoring/alerts/deleteAlert:\x01*BEP\x01ZAgithub.com/VertaAI/modeldb/protos/gen/go/protos/public/monitoringb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'monitoring.Alert_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001ZAgithub.com/VertaAI/modeldb/protos/gen/go/protos/public/monitoring'
  _ALERT_NOTIFICATIONCHANNELSENTRY._options = None
  _ALERT_NOTIFICATIONCHANNELSENTRY._serialized_options = b'8\001'
  _ALERTSERVICE.methods_by_name['createNotificationChannel']._options = None
  _ALERTSERVICE.methods_by_name['createNotificationChannel']._serialized_options = b'\202\323\344\223\0028\"3/api/v1/monitoring/alerts/createNotificationChannel:\001*'
  _ALERTSERVICE.methods_by_name['updateNotificationChannel']._options = None
  _ALERTSERVICE.methods_by_name['updateNotificationChannel']._serialized_options = b'\202\323\344\223\0028\"3/api/v1/monitoring/alerts/updateNotificationChannel:\001*'
  _ALERTSERVICE.methods_by_name['findNotificationChannel']._options = None
  _ALERTSERVICE.methods_by_name['findNotificationChannel']._serialized_options = b'\202\323\344\223\0026\"1/api/v1/monitoring/alerts/findNotificationChannel:\001*'
  _ALERTSERVICE.methods_by_name['deleteNotificationChannel']._options = None
  _ALERTSERVICE.methods_by_name['deleteNotificationChannel']._serialized_options = b'\202\323\344\223\0028*3/api/v1/monitoring/alerts/deleteNotificationChannel:\001*'
  _ALERTSERVICE.methods_by_name['createAlert']._options = None
  _ALERTSERVICE.methods_by_name['createAlert']._serialized_options = b'\202\323\344\223\002*\"%/api/v1/monitoring/alerts/createAlert:\001*'
  _ALERTSERVICE.methods_by_name['updateAlert']._options = None
  _ALERTSERVICE.methods_by_name['updateAlert']._serialized_options = b'\202\323\344\223\002*\"%/api/v1/monitoring/alerts/updateAlert:\001*'
  _ALERTSERVICE.methods_by_name['updateAlertStatus']._options = None
  _ALERTSERVICE.methods_by_name['updateAlertStatus']._serialized_options = b'\202\323\344\223\0020\"+/api/v1/monitoring/alerts/updateAlertStatus:\001*'
  _ALERTSERVICE.methods_by_name['findAlert']._options = None
  _ALERTSERVICE.methods_by_name['findAlert']._serialized_options = b'\202\323\344\223\002(\"#/api/v1/monitoring/alerts/findAlert:\001*'
  _ALERTSERVICE.methods_by_name['listAlertHistory']._options = None
  _ALERTSERVICE.methods_by_name['listAlertHistory']._serialized_options = b'\202\323\344\223\002/\"*/api/v1/monitoring/alerts/listAlertHistory:\001*'
  _ALERTSERVICE.methods_by_name['deleteAlert']._options = None
  _ALERTSERVICE.methods_by_name['deleteAlert']._serialized_options = b'\202\323\344\223\002**%/api/v1/monitoring/alerts/deleteAlert:\001*'
  _NOTIFICATIONCHANNELTYPEENUM._serialized_start=169
  _NOTIFICATIONCHANNELTYPEENUM._serialized_end=249
  _NOTIFICATIONCHANNELTYPEENUM_NOTIFICATIONCHANNELTYPE._serialized_start=200
  _NOTIFICATIONCHANNELTYPEENUM_NOTIFICATIONCHANNELTYPE._serialized_end=249
  _NOTIFICATIONCHANNEL._serialized_start=252
  _NOTIFICATIONCHANNEL._serialized_end=553
  _NOTIFICATIONCHANNELSLACKWEBHOOK._serialized_start=555
  _NOTIFICATIONCHANNELSLACKWEBHOOK._serialized_end=601
  _CREATENOTIFICATIONCHANNELREQUEST._serialized_start=604
  _CREATENOTIFICATIONCHANNELREQUEST._serialized_end=1030
  _UPDATENOTIFICATIONCHANNELREQUEST._serialized_start=1032
  _UPDATENOTIFICATIONCHANNELREQUEST._serialized_end=1125
  _FINDNOTIFICATIONCHANNELREQUEST._serialized_start=1128
  _FINDNOTIFICATIONCHANNELREQUEST._serialized_end=1463
  _FINDNOTIFICATIONCHANNELREQUEST_RESPONSE._serialized_start=1346
  _FINDNOTIFICATIONCHANNELREQUEST_RESPONSE._serialized_end=1439
  _DELETENOTIFICATIONCHANNELREQUEST._serialized_start=1465
  _DELETENOTIFICATIONCHANNELREQUEST._serialized_end=1512
  _ALERTERTYPEENUM._serialized_start=1514
  _ALERTERTYPEENUM._serialized_end=1596
  _ALERTERTYPEENUM_ALERTERTYPE._serialized_start=1533
  _ALERTERTYPEENUM_ALERTERTYPE._serialized_end=1596
  _ALERTSTATUSENUM._serialized_start=1598
  _ALERTSTATUSENUM._serialized_end=1688
  _ALERTSTATUSENUM_ALERTSTATUS._serialized_start=1617
  _ALERTSTATUSENUM_ALERTSTATUS._serialized_end=1688
  _EVALUATIONFREQUENCYENUM._serialized_start=1690
  _EVALUATIONFREQUENCYENUM._serialized_end=1788
  _EVALUATIONFREQUENCYENUM_EVALUATIONFREQUENCY._serialized_start=1717
  _EVALUATIONFREQUENCYENUM_EVALUATIONFREQUENCY._serialized_end=1788
  _AGGREGATIONWINDOWENUM._serialized_start=1790
  _AGGREGATIONWINDOWENUM._serialized_end=1884
  _AGGREGATIONWINDOWENUM_AGGREGATIONWINDOW._serialized_start=1815
  _AGGREGATIONWINDOWENUM_AGGREGATIONWINDOW._serialized_end=1884
  _ALERT._serialized_start=1887
  _ALERT._serialized_end=2827
  _ALERT_NOTIFICATIONCHANNELSENTRY._serialized_start=2745
  _ALERT_NOTIFICATIONCHANNELSENTRY._serialized_end=2804
  _ALERTFIXED._serialized_start=2829
  _ALERTFIXED._serialized_end=2918
  _ALERTRANGE._serialized_start=2920
  _ALERTRANGE._serialized_end=3006
  _ALERTREFERENCE._serialized_start=3008
  _ALERTREFERENCE._serialized_end=3107
  _CREATEALERTREQUEST._serialized_start=3109
  _CREATEALERTREQUEST._serialized_end=3172
  _UPDATEALERTREQUEST._serialized_start=3174
  _UPDATEALERTREQUEST._serialized_end=3237
  _FINDALERTREQUEST._serialized_start=3240
  _FINDALERTREQUEST._serialized_end=3658
  _FINDALERTREQUEST_RESPONSE._serialized_start=3563
  _FINDALERTREQUEST_RESPONSE._serialized_end=3640
  _DELETEALERTREQUEST._serialized_start=3660
  _DELETEALERTREQUEST._serialized_end=3693
  _UPDATEALERTSTATUSREQUEST._serialized_start=3696
  _UPDATEALERTSTATUSREQUEST._serialized_end=3857
  _LISTALERTHISTORYREQUEST._serialized_start=3859
  _LISTALERTHISTORYREQUEST._serialized_end=3968
  _LISTALERTHISTORYREQUEST_RESPONSE._serialized_start=3898
  _LISTALERTHISTORYREQUEST_RESPONSE._serialized_end=3968
  _LISTALERTHISTORYITEM._serialized_start=3971
  _LISTALERTHISTORYITEM._serialized_end=4153
  _ALERTSERVICE._serialized_start=4156
  _ALERTSERVICE._serialized_end=5818
# @@protoc_insertion_point(module_scope)
