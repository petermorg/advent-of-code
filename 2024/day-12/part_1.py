FILEPATH = 'input.txt'

def main():
    lines = parse_input()

    print(lines)

    points_seen = set()
    fencing_cost = 0

    for row_ix, row in enumerate(lines):
        for col_ix, region in enumerate(row):
            point = (row_ix, col_ix)

            # skip if already seen
            if point in points_seen:
                continue

            area, perimeter, extra_points = find_region_stats(lines, point)
            points_seen.update(extra_points)
            fencing_cost += calculate_fencing_cost(area, perimeter)

    print(fencing_cost)


def find_region_stats(
        lines: list[str], 
        starting_point: tuple[int, int],
        points_seen: set[tuple[int, int]] = None
        ) -> tuple[int, int, set[tuple[int, int]]]:
    
    area = 0
    perimeter = 0
    if points_seen is None:
        points_seen = set()

    region = get_region(lines, starting_point)
    assert region is not None

    points_seen.add(starting_point)

    area += 1
    for surrounding_point in get_surrounding_points(starting_point):
        if surrounding_point in points_seen:
            continue
        elif get_region(lines, surrounding_point) != region:
            perimeter += 1
        else:
            extra_area, extra_perimeter, extra_points = find_region_stats(lines, surrounding_point, points_seen)
            area += extra_area
            perimeter += extra_perimeter
            points_seen.update(extra_points)

    return area, perimeter, points_seen


def calculate_fencing_cost(area: int, perimeter: int) -> int:
    return area * perimeter


def get_surrounding_points(point: tuple[int, int]) -> list[tuple[int, int]]:
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in offsets:
        yield (point[0] + dx, point[1] + dy)


def parse_input() -> list[str]:
    with open(FILEPATH, 'r') as file:
        return [line.strip() for line in file]


def get_region(lines: list[str], point: tuple[int, int]) -> str | None:
    try:
        if point[0] < 0 or point[1] < 0:
            raise IndexError('Negative indexes not allowed')
        return lines[point[0]][point[1]]
    except IndexError:
        return None


if __name__ == '__main__':
    main()