package io.hacksy.util;

import java.util.regex.Pattern;

public class Util {
  private static final Pattern pattern = Pattern.compile(".*[dD]ay(\\d\\d).*");

  public static String getDayFromClassName(String className) {
    var m = pattern.matcher(className);
    if (m.find()) {
      return m.group(1).toLowerCase();
    } else {
      throw new RuntimeException("Day not found in '" + className + "'");
    }
  }
}
