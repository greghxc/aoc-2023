import re

import file_util


def process_card(line: str) -> int:
    data_without_card_number = line.split(": ")[1]
    winning_numbers, card_numbers = data_without_card_number.split(" | ")
    winning_numbers = set(re.findall("\\d+", winning_numbers))
    card_numbers = set(re.findall("\\d+", card_numbers))
    return len(winning_numbers.intersection(card_numbers))


def part_one(file_name: str) -> int:
    lines = file_util.get_all_lines(file_name)
    scores = []
    for line in lines:
        match_count = process_card(line)
        scores.append(int(2**(match_count - 1)))
    return sum(scores)


def part_two(file_name: str):
    lines = file_util.get_all_lines(file_name)
    card_counts = [1 for _line in lines]
    for i, line in enumerate(lines):
        match_count = process_card(line)
        for i_to_update in range(i + 1, i + 1 + match_count):
            card_counts[i_to_update] += 1 * card_counts[i]
    return sum(card_counts)


if __name__ == "__main__":
    print(f"Part 1: {part_one('input/input.txt')}")
    print(f"Part 2: {part_two('input/input.txt')}")
