package ai.verta.modeldb.common.futures;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.function.Function;
import java.util.stream.Collectors;

public class BatchLoader<T, R> {
  private final Function<List<T>, InternalFuture<List<R>>> processor;
  private final FutureExecutor executor;
  private static final int MAX_BATCH_SIZE = 1000;

  public BatchLoader(
      Function<List<T>, InternalFuture<List<R>>> processor, FutureExecutor executor) {
    this.processor = processor;
    this.executor = executor;
  }

  public InternalFuture<List<R>> loadAll(List<T> ids) {
    if (ids.isEmpty()) return InternalFuture.completedInternalFuture(List.of());

    var localList = new ArrayList<T>(MAX_BATCH_SIZE);
    var resultsList = new ArrayList<InternalFuture<List<R>>>();
    for (final var id : ids) {
      localList.add(id);
      if (localList.size() >= MAX_BATCH_SIZE) {
        resultsList.add(processor.apply(localList));
        localList = new ArrayList<T>(MAX_BATCH_SIZE);
      }
    }
    if (!localList.isEmpty()) {
      resultsList.add(processor.apply(localList));
    }

    return InternalFuture.sequence(resultsList, executor)
        .thenApply(
            x -> x.stream().flatMap(Collection::stream).collect(Collectors.toList()), executor);
  }
}
