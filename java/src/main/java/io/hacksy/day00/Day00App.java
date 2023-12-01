package io.hacksy.day00;

import io.hacksy.day01.Day01App;
import io.hacksy.util.FileUtil;
import io.hacksy.util.Performance;
import io.hacksy.util.Util;
import java.io.File;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Day00App {
  public static void main(String[] args) {
    Logger logger = LoggerFactory.getLogger(Day01App.class);
    var processor = new Day00Processor();
    var day = Util.getDayFromClassName(processor.getClass().getSimpleName());

    File file = FileUtil.getResourceFile("input/day" + day + "/input.txt");

    var partOne = Performance.timeAndPrint(() ->
        String.format(
            "Day %s - Part 1: %s", day,
            processor.partOne(FileUtil.fileToList(file))
        )
    );
    logger.info(partOne);

    var partTwo = Performance.timeAndPrint(() ->
        String.format(
            "Day %s - Part 2: %s", day,
            processor.partTwo(FileUtil.fileToList(file))
        )
    );
    logger.info(partTwo);
  }
}
