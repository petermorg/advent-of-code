FILEPATH = 'input.txt'

def main():
    tests = parse_input()
    
    valid_tests = [test for test in tests if is_test_valid(test)]
    valid_test_total = sum(test[0] for test in valid_tests)
    
    print(f"{valid_test_total=}")


def parse_input() -> list[tuple[int, list[int]]]:
    tests = []

    with open(FILEPATH, 'r') as file:
        for line in file:
            first_part, second_part = line.split(': ')

            tests.append((int(first_part), list(map(int, second_part.split()))))

    return tests


def is_test_valid(test: tuple[int, list[int]]) -> bool:
    result, operands = test

    def depth_first_search(current, index) -> bool:
        if index == len(operands):
            return current == result
        
        add_path = depth_first_search(current + operands[index], index + 1)
        multiply_path = depth_first_search(current * operands[index], index + 1)
        # part 2
        concat_path = depth_first_search(int(str(current) + str(operands[index])), index + 1)

        return add_path or multiply_path or concat_path

    return depth_first_search(operands[0],1)


if __name__ == '__main__':
    main()