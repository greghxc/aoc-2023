from unittest import TestCase
import day_02


class TestDay02(TestCase):
    def test_part_one(self):
        self.assertEquals(day_02.part_one("input/test1.txt"), 8)

    def test_part_two(self):
        self.assertEquals(day_02.part_two("input/test1.txt"), 2286)
