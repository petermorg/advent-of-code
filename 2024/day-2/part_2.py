FILEPATH = 'input.txt'

def main():
    reports = parse_input()

    safe_reports = 0
    for report in reports:

        is_report_safe = scan_report(report, dampers_remaining=1)
        print(f"is_safe : {is_report_safe} - {report}")

        safe_reports += 1 if scan_report(report, dampers_remaining=1) else 0

    print(f"{safe_reports=}")


def parse_input() -> list[list[int]]:
    reports = []
    with open(FILEPATH, 'r') as file:
        for line in file:
            reports.append([int(e) for e in line.strip().split()])

    return reports


def scan_report(report: list[int], dampers_remaining: int) -> bool:

    is_increasing = report[0] < report[1]

    for index in range(len(report) - 1):
        left_value = report[index]
        right_value = report[index + 1]

        if check_pair(left_value, right_value, is_increasing):
            continue
        elif dampers_remaining == 0:
            return False
        else:
            report_without_left_value = report.copy()
            report_without_left_value.pop(index)
            report_without_right_value = report.copy()
            report_without_right_value.pop(index + 1)
            report_without_initial_value = report.copy()
            report_without_initial_value.pop(0)

            return \
                scan_report(report_without_left_value, dampers_remaining - 1) or \
                scan_report(report_without_right_value, dampers_remaining - 1) or \
                scan_report(report_without_initial_value, dampers_remaining - 1)


    return True


def check_pair(left_value: int, right_value: int, is_report_increasing: bool):
    difference = right_value - left_value
    if not (1 <= abs(difference) <= 3):
        # difference too large
        return False
    
    if not is_report_increasing is None and (difference > 0) != is_report_increasing:
        # change in direction
        return False
    
    return True


if __name__ == '__main__':
    main()