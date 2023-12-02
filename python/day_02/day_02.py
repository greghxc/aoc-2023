import file_util
import math
import re


def part_one(file_name: str) -> int:
    def valid(line: str) -> bool:
        max_cubes = {"red": 12, "green": 13, "blue": 14}
        for found in re.findall("(\\d+ [a-z]+)", line):
            count, color = found.split(" ")
            if int(count) > max_cubes[color]:
                return False
        return True

    lines = file_util.get_all_lines(file_name)
    valid_games = [i + 1 for i, line in enumerate(lines) if valid(line)]

    return sum(valid_games)


def part_two(file_name: str) -> int:
    def product_of_line(line: str) -> int:
        counts = {}
        for found in re.findall("(\\d+ [a-z]+)", line):
            count, color = found.split(" ")
            counts[color] = max(counts.get(color, 0), int(count))
        return math.prod(counts.values())

    lines = file_util.get_all_lines(file_name)
    products = [product_of_line(line) for line in lines]
    return sum(products)


if __name__ == "__main__":
    print(f"Part 1: {part_one('input/input.txt')}")
    print(f"Part 2: {part_two('input/input.txt')}")
