FILEPATH = 'input.txt'
CACHE = {}


def main():
    stones = parse_input()
    blinks_remaining = 25

    while blinks_remaining > 0:
        stones = blink(stones)
        blinks_remaining -= 1

    print(len(stones))

def parse_input() -> list[str]:
    with open(FILEPATH, 'r') as file:
        return file.read().strip().split()


def blink(stones: list[str]) -> list[str]:
    new_stones = []

    for stone in stones:
        if stone not in CACHE:
            CACHE[stone] = calculate_next_stones(stone)

        new_stones += CACHE[stone]

    return new_stones


def calculate_next_stones(stone: str) -> list[str]:
    value = int(stone)

    if value == 0:
        return['1']
    elif len(stone) % 2 == 0:
        midpoint = len(stone) // 2
        return [str(int(stone[:midpoint])), str(int(stone[midpoint:]))]
    else:
        return [str(value * 2024)]


if __name__ == '__main__':
    main()