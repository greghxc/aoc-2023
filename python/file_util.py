def get_all_lines(file_name: str) -> list[str]:
    with open(file_name) as file:
        return [line.rstrip() for line in file.readlines()]


def get_all_lines_as_int(file_name: str) -> list[int]:
    with open(file_name) as file:
        return [int(line.rstrip()) for line in file.readlines()]
