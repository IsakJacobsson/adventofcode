with open("input.txt", "r") as f:
    input = f.read()

s = input.strip().split("\n\n")

s = [[int(n) for n in elf.split("\n")] for elf in s]

print(max([sum(x) for x in s]))

s = sorted([sum(x) for x in s], reverse=True)

print(sum(s[:3]))
