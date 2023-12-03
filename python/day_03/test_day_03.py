from unittest import TestCase
import day_03


class TestDay03(TestCase):
    def test_part_one(self):
        self.assertEquals(day_03.part_one("input/test1.txt"), 4361)

    def test_part_two(self):
        self.assertEquals(day_03.part_two("input/test1.txt"), 467835)
