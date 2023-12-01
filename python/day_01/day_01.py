import file_util
import re


DIGITS: list[str] = [
    "zero", "one", "two", "three", "four",
    "five", "six", "seven", "eight", "nine"
]
DIGIT_VALUES: dict[str, str] = {v: str(i) for i, v in enumerate(DIGITS)}


def part_one(file_name: str) -> int:
    def get_number(line: str) -> int:
        found = re.findall("\\d", line)
        return int(found[0] + found[-1])

    lines = file_util.get_all_lines(file_name)
    return sum([get_number(line) for line in lines])


def part_two(file_name: str) -> int:
    def get_number(line: str) -> int:
        regex = f"(?=(\\d|{'|'.join(DIGITS)}))"
        found = re.findall(regex, line)
        first_and_last = found[0] + found[-1]
        for key in DIGIT_VALUES.keys():
            first_and_last = first_and_last.replace(key, DIGIT_VALUES[key])
        return int(first_and_last)

    lines = file_util.get_all_lines(file_name)
    return sum([get_number(line) for line in lines])


if __name__ == "__main__":
    print(f"Part 1: {part_one('input/input.txt')}")
    print(f"Part 2: {part_two('input/input.txt')}")
