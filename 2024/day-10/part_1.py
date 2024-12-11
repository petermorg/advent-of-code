FILEPATH = 'input.txt'


def main():
    lines = parse_input()

    trailheads = find_trailheads(lines)

    trail_count = sum([count_trails(lines, trailhead) for trailhead in trailheads])

    print(f"{trail_count=}")


def parse_input() -> list[str]:
    with open(FILEPATH, 'r') as file:
        lines = [line.strip() for line in file]

    return lines


def find_trailheads(lines: list[str]) -> list[tuple[int, int]]:
    trailheads = []
    
    for row_ix, line in enumerate(lines):
        for col_ix, numeral in enumerate(line):
            if numeral == '0':
                trailheads.append((row_ix, col_ix))
    
    return trailheads


def count_trails(lines: list[str], trailhead: tuple[int, int]) -> int:

    def get_trailends(point: tuple[int, int], height: int) -> set[tuple[int, int]]:
        if height == 9:
            return {point}
        
        trailheads = set()
        for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            next_point = (point[0] + direction[0], point[1] + direction[1])

            try:
                if next_point[0] < 0 or next_point[1] < 0:
                    raise IndexError('Negative indexes not allowed')
                next_height = int(lines[next_point[0]][next_point[1]])
            except IndexError:
                continue
            
            if next_height != height + 1:
                continue

            trailheads = trailheads.union(get_trailends(next_point, next_height))

        return trailheads

    trailends = get_trailends(trailhead, 0)

    return len(trailends)

if __name__ == '__main__':
    main()