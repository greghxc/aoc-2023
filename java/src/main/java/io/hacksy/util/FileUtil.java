package io.hacksy.util;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Objects;
import java.util.stream.Stream;

public class FileUtil {
  public static File getResourceFile(String path) {
    ClassLoader loader = Thread.currentThread().getContextClassLoader();

    try {
      var url = Objects.requireNonNull(loader.getResource(path));
      return new File(url.getFile());
    } catch (NullPointerException npe) {
      throw new FileUtilException(String.format("Unable to load resource: %s", path));
    }
  }

  public static List<Integer> fileToList(File file) {
    try (Stream<String> stream = Files.lines(Paths.get(file.toURI()))) {
      return stream.map(Integer::parseInt).toList();
    } catch (IOException e) {
      throw new FileUtilException(e.getMessage());
    }
  }

  public static List<String> fileToStringList(File file) {
    try (Stream<String> stream = Files.lines(Paths.get(file.toURI()))) {
      return stream.toList();
    } catch (IOException e) {
      throw new FileUtilException(e.getMessage());
    }
  }

  static class FileUtilException extends RuntimeException {
    FileUtilException(String msg) {
      super(msg);
    }
  }
}
