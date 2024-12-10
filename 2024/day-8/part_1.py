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
            antinodes.update(get_antinodes(position_1, position_2))
    
    in_bound_antinodes = [
        node for node in antinodes 
        if 0 <= node[0] < len(lines) 
        and 0 <= node[1] < len(lines[node[0]])
    ]

    print(len(in_bound_antinodes))


def parse_input() -> list[str]:
    with open(FILEPATH, 'r') as file:
        lines = [line.strip() for line in file]

    return lines


def get_antinodes(position_1: tuple[int, int], position_2: tuple[int, int]) -> list[tuple[int, int]]:
    row_diff = position_2[0] - position_1[0]
    col_diff = position_2[1] - position_1[1]

    return [
        (position_1[0] - row_diff, position_1[1] - col_diff),
        (position_2[0] + row_diff, position_2[1] + col_diff)
    ]


if __name__ == '__main__':
    main()