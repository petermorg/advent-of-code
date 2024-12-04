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

    starting_points = find_starting_points(lines, word[0])
    direction_vectors = get_direction_vectors()

    for point in starting_points:
        for direction in direction_vectors:
            if is_word_present(lines, point, direction):
                word_count += 1

    return word_count


def find_starting_points(lines: list[str], starting_letter: str) -> list[tuple[int, int]]:
    starting_points = []

    for row_ix, line in enumerate(lines):
        for col_ix, letter in enumerate(line):
            if letter == starting_letter:
                starting_points.append((row_ix, col_ix))

    return starting_points


def get_direction_vectors() -> list[tuple[int, int]]:
    return [
        (r, c) 
        for r in range(-1, 2) 
        for c in range(-1, 2) 
        if (r, c) != (0, 0)
    ]


def is_word_present(
        lines: list[str],
        starting_point: tuple[int, int],
        direction_vector: tuple[int, int],
        word: str = 'XMAS'
        ) -> bool:
    
    assert lines[starting_point[0]][starting_point[1]] == word[0]

    for index, letter in enumerate(word):
        row_index = starting_point[0] + (direction_vector[0] * index)
        col_index = starting_point[1] + (direction_vector[1] * index)
        
        try:
            if row_index < 0 or col_index < 0:
                raise IndexError('Negative indexes not allowed')
            if not is_letter_matching(lines, (row_index, col_index), letter):
                return False
        except IndexError:
            # index out of range - so not a word
            return False
    
    return True


def is_letter_matching(lines: list[str], point: tuple[int, int], letter: str) -> bool:
    return lines[point[0]][point[1]] == letter


if __name__ == '__main__':
    main()