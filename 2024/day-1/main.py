FILEPATH = 'input.txt'

def main():
    left_list, right_list = parse_input()

    distance = measure_distance(left_list, right_list)
    print(f"{distance=}")

    similarity = measure_similarity(left_list, right_list)
    print(f"{similarity=}")


def parse_input() -> tuple[list[int], list[int]]:
    list_1 = []
    list_2 = []

    with open(FILEPATH, 'r') as file:
        for line in file:
            parts = line.strip().split('   ')
            assert len(parts) == 2

            list_1.append(int(parts[0]))
            list_2.append(int(parts[1]))

    return list_1, list_2 


def measure_distance(list_1: list[int], list_2: list[int]) -> int:
    # sort lists
    list_1.sort()
    list_2.sort()

    # sum distances
    assert len(list_1) == len(list_2)
    return sum(abs(a - b) for a, b in zip(list_1, list_2))


def measure_similarity(list_1: list[int], list_2: list[int]) -> int:
    list_2_counts = {}
    for element in list_2:
        list_2_counts[element] = list_2_counts.get(element, 0) + 1

    return sum(element * list_2_counts.get(element, 0) for element in list_1)


if __name__ == '__main__':
    main()