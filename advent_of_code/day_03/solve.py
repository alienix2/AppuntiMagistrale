from aocd import get_data
from aocd import submit
import regex as re

get_data = get_data(day=3, year=2024)

# Part a
real_muls = re.findall(r"\bmul\(\d+,\d+\)", get_data)

total = 0
for real_mul in real_muls:
    a, b = map(int, re.findall(r"\d+", real_mul))
    total += a * b

print(total)
submit(total, part="a", day=3, year=2024)

# Part b
real_muls = re.findall(r"(?:mul\(\d+,\d+\)|do\(\)|don't\(\))", get_data)
print(real_muls)

total = 0
enabled = True
for operation in real_muls:
    if "do()" in operation:
        enabled = True
    elif "don't()" in operation:
        enabled = False
    elif "mul" in operation and enabled == True:
        a, b = map(int, re.findall(r"\d+", operation))
        total += a * b

print(total)
submit(total, part="b", day=3, year=2024)
