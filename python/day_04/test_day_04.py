from unittest import TestCase
import day_04


class TestDay04(TestCase):
    def test_part_one(self):
        self.assertEquals(day_04.part_one("input/test1.txt"), 13)

    def test_part_two(self):
        self.assertEquals(day_04.part_two("input/test1.txt"), 30)
