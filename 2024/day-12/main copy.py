FILEPATH = 'input.txt'

def main():
    lines = parse_input()

    points_seen = set()
    fencing_cost = 0


    for row_ix, row in enumerate(lines):
        for col_ix, region in enumerate(row):
            point = (row_ix, col_ix)

            # skip if already seen
            if point in points_seen:
                continue

            area, perimeter, extra_points, boundaries = find_region_stats(lines, point)
            
            print(f"Point: {point}, Reg: {region}, A: {area}, L(bound): {len(boundaries)}")
            print(f"L(pl): {get_plane_count(list(boundaries))}")

            points_seen.update(extra_points)
            # fencing_cost += calculate_fencing_cost(area, perimeter)  # part 1
            fencing_cost += calculate_fencing_cost(area, get_plane_count(list(boundaries)))

    print(fencing_cost)


def find_region_stats(
        lines: list[str], 
        starting_point: tuple[int, int],
        points_seen: set[tuple[int, int]] = None,
        ) -> tuple[int, int, set[tuple[int, int]], set[tuple[int, int, bool]]]:
    
    area = 0
    perimeter = 0
    if points_seen is None:
        points_seen = set()
    boundaries = set()

    region = get_region(lines, starting_point)
    assert region is not None

    points_seen.add(starting_point)

    area += 1
    for surrounding_point in get_surrounding_points(starting_point):
        if surrounding_point in points_seen:
            continue
        elif get_region(lines, surrounding_point) != region:
            perimeter += 1
            boundaries.add(get_boundary(starting_point, surrounding_point))
        else:
            extra_area, extra_perimeter, extra_points, extra_planes = find_region_stats(lines, surrounding_point, points_seen)
            area += extra_area
            perimeter += extra_perimeter
            points_seen.update(extra_points)
            boundaries.update(extra_planes)

    return area, perimeter, points_seen, boundaries

# part 1
# def calculate_fencing_cost(area: int, perimeter: int) -> int:
#     return area * perimeter


def calculate_fencing_cost(area: int, plane_count: int) -> int:
    return area * plane_count


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


def get_boundary(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int, bool]:
    difference = (x[0] - y[0], x[1] - y[1])
    assert difference[0] == 0 or difference[1] == 0

    x_plane = difference[1] == 0
    return (max(x[0], y[0]), max(x[1], y[1]), x_plane)


def get_plane_count(boundaries: list[tuple[int, int, bool]]) -> int:
    plane_count = 0

    x_plane_boundaries = [b for b in boundaries if b[2] == True]
    for boundary_row in set(b[0] for b in x_plane_boundaries):
        columns = [b[1] for b in x_plane_boundaries if b[0] == boundary_row]
        columns.sort()
        plane_count += count_contiguous_sections(columns)

    y_plane_boundaries = [b for b in boundaries if b[2] == False]
    for boundary_col in set(b[1] for b in y_plane_boundaries):
        rows = [b[0] for b in y_plane_boundaries if b[1] == boundary_col]
        rows.sort()
        plane_count += count_contiguous_sections(rows)


    # check for cruciform boundaries and increment planes by two if found
    grouped_boundaries = {}
    for row_ix, col_ix, plane in boundaries:
        point = (row_ix, col_ix)
        if point not in grouped_boundaries:
            grouped_boundaries[point] = set()
        grouped_boundaries[point].add(plane)

    for point, planes in grouped_boundaries.items():
        if len(planes) > 1:
            if (point[0] - 1, point[1], False) in boundaries \
            and (point[0], point[1] -1, True) in boundaries:
                plane_count += 2
    

    return plane_count


def count_contiguous_sections(numbers: list[int]) -> int:    
    count = 1
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1] + 1:
            count += 1
    
    return count


if __name__ == '__main__':
    main()