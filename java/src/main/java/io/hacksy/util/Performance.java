package io.hacksy.util;

import java.util.function.Supplier;

public class Performance {
  public static String timeAndPrint(Supplier<String> stringSupplier) {
    long startTime = System.nanoTime();
    String result = stringSupplier.get();
    long endTime = System.nanoTime();
    long duration = (endTime - startTime);

    return String.format("Completed in %s seconds:", duration / 1_000_000_000.0)
           + String.format(" - %s", result);
  }
}