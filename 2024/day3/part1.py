import re

input = open("input.txt").read()
muls = re.findall(r"mul\((\d+),(\d+)\)", input)

res = 0
for mul in muls:
    res += int(mul[0]) * int(mul[1])

print(res)