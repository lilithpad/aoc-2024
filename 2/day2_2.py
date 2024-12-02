reports = []

with open("input", "r") as input:
    for line in input:
        report = []
        line = line.split(" ")
        for reading in line:
            report.append(int(reading))
        reports.append(report)

def is_safe(report):
    is_increasing = None
    is_safe = True
    for i in range(len(report)):
        if i == 0:
            if report[i] < report[i + 1]:
                is_increasing = True
        if i != len(report) - 1:
            difference = 0
            if is_increasing:
                difference = report[i + 1] - report[i]
            elif not is_increasing:
                difference = report[i] - report[i + 1]
            if 1 <= difference <= 3:
                continue
            else:
                is_safe = False

    return is_safe

def is_safe_dampened(report, max_unsafe = 1):
    return sum([is_safe(report[:i] + report[i + 1:]) for i in range(len(report))]) >= max_unsafe

print(sum([is_safe_dampened(report) for report in reports]))
