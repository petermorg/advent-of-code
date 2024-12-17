import re

FILEPATH = 'input.txt'


def main():
    machine_data = parse_input()

    cost = 0
    for machine in machine_data:
        extra_cost = find_minimum_spend(machine[0], machine[1], machine[2])
        cost += extra_cost if extra_cost else 0

    print(cost)

def parse_input() -> list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]]:
    with open(FILEPATH, 'r') as file:

        string = file.read().strip()
        pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"

        matches = re.findall(pattern, string)

        data = []
        for match in matches:
            data.append((
                (int(match[0]), int(match[1])),
                (int(match[2]), int(match[3])),
                (int(match[4]), int(match[5]))
            ))

        return data


def find_minimum_spend(
        vector_a: tuple[int, int], 
        vector_b: tuple[int, int], 
        prize_location: tuple[int, int]
        ) -> int | None:
    
    cost_a = 3
    cost_b = 1
    
    count_b = (
        vector_a[0] * prize_location[1]
        - vector_a[1] * prize_location[0]
    
    ) / (
        vector_a[0] * vector_b[1]
        - vector_a[1] * vector_b[0]
    )

    count_a = (
        prize_location[0] - vector_b[0] * count_b
    ) / vector_a[0]

    if count_a.is_integer() and count_b.is_integer():
        return cost_a * count_a + cost_b * count_b
    else:
        return None

if __name__ == '__main__':
    main()