import file_util


def pad_input(input: list[str]) -> list[str]:
    padded_width = len(input[0]) + 2
    lr_padded = [line.center(padded_width, ".") for line in input]
    return [("." * padded_width)] + lr_padded + [("." * padded_width)]


def adjacent_chars(line_number: int, char_number: int) -> list[tuple[int, int]]:
    up = line_number - 1
    down = line_number + 1
    left = char_number - 1
    right = char_number + 1

    return [
        (up, char_number), (up, right), (line_number, right), (down, right),
        (down, char_number),(down, left), (line_number, left), (up, left),
    ]


def part_one(file_name: str) -> int:
    lines = file_util.get_all_lines(file_name)
    lines = pad_input(lines)

    not_symbols = {str(i) for i in set([*range(0, 10)] + ['.'])}
    parts = []
    for line_number, line in enumerate(lines):
        is_symbol_adjacent = False
        accumulated_number = ""
        for char_number, char in enumerate(line):
            if char.isdigit():
                accumulated_number += char
                results = {lines[result[0]][result[1]] for result in adjacent_chars(line_number, char_number)}
                if len(results.intersection(not_symbols)) != len(results):
                    is_symbol_adjacent = True
            else:
                if accumulated_number and is_symbol_adjacent:
                    parts += [accumulated_number]
                accumulated_number = ""
                is_symbol_adjacent = False

    return sum([int(i) for i in parts])


def part_two(file_name: str):
    lines = file_util.get_all_lines(file_name)
    lines = pad_input(lines)

    potential_gears = {}
    for line_number, line in enumerate(lines):
        gear_coords = set()
        accumulated_number = ""
        for char_number, char in enumerate(line):
            if char.isdigit():
                accumulated_number += char
                adj_coords = adjacent_chars(line_number, char_number)
                for coord in adj_coords:
                    if lines[coord[0]][coord[1]] == "*":
                        gear_coords.add(coord)
            else:
                if accumulated_number and len(gear_coords):
                    for coord in gear_coords:
                        potential_gears[coord] = potential_gears.get(coord, []) + [accumulated_number]
                accumulated_number = ""
                gear_coords = set()

    ratios = [int(v[0]) * int(v[1]) for k, v in potential_gears.items() if len(v) == 2]
    return sum(ratios)


if __name__ == "__main__":
    print(f"Part 1: {part_one('input/input.txt')}")
    print(f"Part 2: {part_two('input/input.txt')}")
