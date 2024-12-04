FILEPATH = 'input.txt'

def main():
    lines = parse_input()
    word_count = count_words(lines)
    print(f"{word_count=}")


def parse_input() -> list[str]:
    with open(FILEPATH, 'r') as file:
        lines = [line.strip() for line in file]
    return lines
            

def count_words(lines: list[str], word: str = 'XMAS'):
    word_count = 0

    starting_points = find_starting_points(lines, 'A')

    for point in starting_points:
        if is_cross_present(lines, point):
            word_count += 1

            print(f"{word_count} Found for {point}")

    return word_count


def find_starting_points(lines: list[str], starting_letter: str) -> list[tuple[int, int]]:
    starting_points = []

    for row_ix, line in enumerate(lines):
        for col_ix, letter in enumerate(line):
            if letter == starting_letter:
                starting_points.append((row_ix, col_ix))

    return starting_points


def is_cross_present(
        lines: list[str],
        starting_point: tuple[int, int],
        ) -> bool:
    
    try:
        if starting_point[0] < 1 or starting_point[1] < 1:
            raise IndexError("Too close to the edge")

        # upper-right and lower-left letters
        right_diag_1 = get_letter(lines, (starting_point[0] - 1, starting_point[1] + 1))
        right_diag_2 = get_letter(lines, (starting_point[0] + 1, starting_point[1] - 1))

        # upper-left and lower-right letters
        left_diag_1 = get_letter(lines, (starting_point[0] - 1, starting_point[1] - 1))
        left_diag_2 = get_letter(lines, (starting_point[0] + 1, starting_point[1] + 1))
    except IndexError:
        return False
    
    reference_letters = {'M', 'S'}

    return \
        {right_diag_1, right_diag_2} == reference_letters and \
        {left_diag_1, left_diag_2} == reference_letters


def get_letter(lines: list[str], point: tuple[int, int]) -> str:
    return lines[point[0]][point[1]]


if __name__ == '__main__':
    main()