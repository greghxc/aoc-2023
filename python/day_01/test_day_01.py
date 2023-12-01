from unittest import TestCase
import day_01


class TestDay00(TestCase):
    def test_part_one(self):
        self.assertEquals(day_01.part_one("input/test1.txt"), 0)

    def test_part_two(self):
        self.assertEquals(day_01.part_two("input/test1.txt"), 0)
