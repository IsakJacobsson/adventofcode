with open("input.txt", "r") as f:
    s = f.read().strip()

pairs = s.split("\n")
res = 0

for pair in pairs:
    elf1, elf2 = pair.split(",")
    elf1_1, elf1_2 = elf1.split("-")
    elf2_1, elf2_2 = elf2.split("-")
    if int(elf1_1) <= int(elf2_1) and int(elf1_2) >= int(elf2_2):
        res += 1
    elif int(elf2_1) <= int(elf1_1) and int(elf2_2) >= int(elf1_2):
        res += 1

print(res)
res = 0

for pair in pairs:
    elf1, elf2 = pair.split(",")
    elf1_1, elf1_2 = elf1.split("-")
    elf2_1, elf2_2 = elf2.split("-")
    inter = set(range(int(elf1_1), int(elf1_2) + 1)) & set(
        range(int(elf2_1), int(elf2_2) + 1)
    )
    if inter:
        res += 1

print(res)
