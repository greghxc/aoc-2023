package io.hacksy.day00;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

import io.hacksy.util.FileUtil;
import io.hacksy.util.Util;
import java.io.File;
import org.junit.jupiter.api.Test;

class Day00ProcessorTest {
  Day00Processor processor = new Day00Processor();

  @Test
  void partOne() {
    File file = FileUtil.getResourceFile("input/day" + getDay() + "/test1.txt");
    var result = processor.partOne(FileUtil.fileToList(file));
    assertThat(result).isEqualTo(5);
  }

  @Test
  void partTwo() {
    File file = FileUtil.getResourceFile("input/day" + getDay() + "/test1.txt");
    var result = processor.partOne(FileUtil.fileToList(file));
    assertThat(result).isEqualTo(5);
  }

  private String getDay() {
    return Util.getDayFromClassName(processor.getClass().getSimpleName());
  }
}