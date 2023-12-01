from unittest import TestCase
import day_00


class TestDay00(TestCase):
    def test_part_one(self):
        self.assertEquals(day_00.part_one("input/test1.txt"), 5)

    def test_part_two(self):
        self.assertEquals(day_00.part_two("input/test1.txt"), 5)
