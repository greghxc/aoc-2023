package io.hacksy.util;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class UtilTest {

  @Test
  void getDayFromClassName() {
    assertThat(Util.getDayFromClassName("Day01Processor")).isEqualTo("01");
  }
}