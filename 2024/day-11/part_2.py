FILEPATH = 'input.txt'

def main():
    original_stones = parse_input()
    blinks = 75

    stones = {}
    for stone in original_stones:
        stones[stone] = stones.get(stone, 0) + 1

    for _ in range(blinks):
        new_stones = {}
        for stone in stones:
            if stone == 0:
                new_stones[1] = new_stones.get(1, 0) + stones[stone]
            else:
                length = len(str(stone))
                if length % 2 == 0:
                    first_new_stone = int(str(stone)[: length // 2])
                    second_new_stone = int(str(stone)[length // 2 :])

                    new_stones[first_new_stone] = new_stones.get(first_new_stone, 0) + stones[stone]
                    new_stones[second_new_stone] = new_stones.get(second_new_stone, 0) + stones[stone]
                else:
                    new_stone = stone * 2024
                    new_stones[new_stone] = new_stones.get(new_stone, 0) + stones[stone]

        stones = new_stones

    stones_count = sum([count for count in stones.values()])
    print(stones_count)


def parse_input() -> list[int]:
    with open(FILEPATH, 'r') as file:
        return list(map(int, file.read().strip().split()))


if __name__ == '__main__':
    main()