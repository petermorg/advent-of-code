import re

FILEPATH = 'input.txt'

def main():
    mul_pairs = parse_input()
    total = sum(a * b for a, b in mul_pairs)
    print(f"{total=}")


def parse_input():

    with open(FILEPATH, 'r') as file:
        instructions = file.read()

    active_instructions = parse_active_instructions(instructions)

    mul_pairs = []
    for instruction in active_instructions:
        print(instruction)
        mul_pairs.extend(parse_mul_pairs(instruction))

    return mul_pairs


def parse_active_instructions(instructions: str) -> list[str]:

    active_instructions = []

    pattern = re.compile(r"^(.+?)(?=don't\(\)|$)|do\(\)(.+?)(?=(?:don't\(\)|$))", re.DOTALL)
    matches = re.finditer(pattern, instructions)

    for match in matches:
        for group in match.groups():
            if group:
                active_instructions.append(group)
    
    return active_instructions
            

def parse_mul_pairs(instructions: str) -> list[tuple[int, int]]:

    mul_pairs = []

    pattern = r".*?mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.finditer(pattern, instructions)
    
    for match in matches:
        mul_pairs.append((
            int(match.group(1)), 
            int(match.group(2))
        ))

    return mul_pairs


if __name__ == '__main__':
    main()
