package io.hacksy.day00;

import java.util.List;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Day00Processor {
  private static final Logger LOG = LoggerFactory.getLogger(Day00Processor.class);

  int partOne(List<Integer> input) {
    return input.stream().mapToInt(Integer::intValue).sum();
  }

  int partTwo(List<Integer> input) {
    return input.stream().mapToInt(Integer::intValue).sum();
  }
}
