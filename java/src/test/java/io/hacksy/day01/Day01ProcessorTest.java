package io.hacksy.day01;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

import io.hacksy.day00.Day00Processor;
import io.hacksy.util.FileUtil;
import io.hacksy.util.Util;
import java.io.File;
import org.junit.jupiter.api.Test;

class Day01ProcessorTest {
  Day01Processor processor = new Day01Processor();

  @Test
  void partOne() {
    File file = FileUtil.getResourceFile("input/day" + getDay() + "/test1.txt");
    var result = processor.partOne(FileUtil.fileToList(file));
    assertThat(result).isEqualTo(0);
  }

  @Test
  void partTwo() {
    File file = FileUtil.getResourceFile("input/day" + getDay() + "/test1.txt");
    var result = processor.partOne(FileUtil.fileToList(file));
    assertThat(result).isEqualTo(0);
  }

  private String getDay() {
    return Util.getDayFromClassName(processor.getClass().getSimpleName());
  }
}