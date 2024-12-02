

def is_report_safe(report: list[int]) -> bool:
    variances = []
    for i in range(len(report) - 1):
        variances.append(report[i] - report[i + 1])
    return (
        all(1 <= i <= 3 for i in variances)
        or
        all(-3 <= i <= -1 for i in variances)
    )

def generate_variations(line: list[int]) -> list[list[int]]:
    variations: list[list[int]] = []
    for i in range(len(line)):
        variations.append(line[:i] + line[i+1:])
    return variations


dat: list[list[int]] = []
with open("input.txt", 'r') as fin:
    for line in fin.readlines():
        dat.append(list(map(int, line.split(" "))))

safe = dampenered = 0
for line in dat:
    if is_report_safe(line):
        safe += 1
    variations = generate_variations(line)
    variations.insert(0, line)
    if any(is_report_safe(v) for v in variations):
        dampenered += 1
print(f"Part1: {safe}")
print(f"Part2: {dampenered}")
