FILEPATH = 'input.txt'

def main():
    reports = parse_input()

    safe_reports = 0
    for report in reports:
        safe_reports += 1 if scan_report(report) else 0

    print(f"{safe_reports=}")


def parse_input() -> list[list[int]]:
    reports = []
    with open(FILEPATH, 'r') as file:
        for line in file:
            reports.append([int(e) for e in line.strip().split()])

    return reports


def scan_report(report: list[int]) -> bool:
    for index in range(len(report)):
        if index == 0:
            continue
        
        difference = report[index] - report[index - 1]
        if not (1 <= abs(difference) <= 3):
            # difference too large
            return False
        
        if index == 1:
            continue
        
        previous_difference = report[index - 1] - report[index - 2]
        if (difference < 0) != (previous_difference < 0):
            # change in direction
            return False
        
    return True


if __name__ == '__main__':
    main()