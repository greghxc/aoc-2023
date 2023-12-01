import file_util


def part_one(file_name: str) -> int:
    result = file_util.get_all_lines_as_int(file_name)
    return sum(result)


def part_two(file_name: str):
    result = file_util.get_all_lines_as_int(file_name)
    return sum(result)


if __name__ == "__main__":
    print(f"Part 1: {part_one('input/input.txt')}")
    print(f"Part 2: {part_two('input/input.txt')}")
