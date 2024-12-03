import re

def get_mul_product_sums(text: str) -> int:
    # match mul(a,b) where a and b are any numbers
    mul_pattern = r'mul\((-?\d+\.?\d*),(-?\d+\.?\d*)\)'
    matches = re.findall(mul_pattern, text)

    total = 0
    for match in matches:
        total += int(match[0]) * int(match[1])
    return total

with open("input.txt", "r") as file:
    dat = file.read()

print(f"Part1: {get_mul_product_sums(dat)}")

running_total = 0
span: list[int] = [0, 0]
dat = "do()" + dat
while span[1] != -1:
    span[0] = dat.find("do()", span[1])
    span[1] = dat.find("don't()", span[0])
    running_total += get_mul_product_sums(dat[span[0]:span[1]])
print(f"Part2: {running_total}")
