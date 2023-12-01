package io.hacksy;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

public class AppTest {
    boolean testVal;

    @BeforeEach
    public void setUp() {
        testVal = true;
    }

    @Test
    @DisplayName("SampleTest")
    public void test01() {
        assertThat(testVal).isTrue();
    }
}
