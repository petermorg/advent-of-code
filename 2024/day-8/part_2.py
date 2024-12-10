from itertools import combinations


FILEPATH = 'input.txt'

def main():
    lines = parse_input()

    antenna_positions = {}
    for row_ix, line in enumerate(lines):
        for col_ix, point in enumerate(line):
            if point != '.':
                antenna_positions[point] = antenna_positions.get(point, []) + [(row_ix, col_ix)]
    
    antinodes = set()
    for positions in antenna_positions.values():
        for position_1, position_2 in combinations(positions, 2):
            antinodes.update(get_antinodes(position_1, position_2, lines))
    
    print(len(antinodes))


def parse_input() -> list[str]:
    with open(FILEPATH, 'r') as file:
        lines = [line.strip() for line in file]

    return lines


def get_antinodes(
        position_1: tuple[int, int], 
        position_2: tuple[int, int],
        lines: list[str]
        ) -> list[tuple[int, int]]:
    row_diff = position_2[0] - position_1[0]
    col_diff = position_2[1] - position_1[1]

    antinodes = []

    position = position_1
    while 0 <= position[0] < len(lines) and 0 <= position[1] < len(lines[position[0]]):
        antinodes.append(position)
        position = (position[0] - row_diff, position[1] - col_diff)

    position = position_2
    while 0 <= position[0] < len(lines) and 0 <= position[1] < len(lines[position[0]]):
        antinodes.append(position)
        position = (position[0] + row_diff, position[1] + col_diff)

    return antinodes



if __name__ == '__main__':
    main()