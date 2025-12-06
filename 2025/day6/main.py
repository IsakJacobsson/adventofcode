with open("input.txt", "r") as f:
    s = f.read()[:-1]

rows = s.split("\n")
nums = [[int(num) for num in nums.split()] for nums in rows[:-1]]
ops = [c for c in rows[-1].split()]

res = 0
for i, op in enumerate(ops):
    colres = 0 if op == "+" else 1
    for r in range(len(nums)):
        if op == "+":
            colres += nums[r][i]
        else:
            colres *= nums[r][i]
    res += colres

print(res)

print("----")

# Part 2

rows = s.split("\n")
nums = rows[:-1]
ops = [c for c in rows[-1].split()]

res = 0
col = len(nums[0]) - 1
current_op_idx = len(ops) - 1
nums_for_op = []

while col >= 0:
    num_str = ""

    # Build the number top down
    for r in range(len(nums)):
        num_c = nums[r][col]
        if num_c != " ":
            num_str += num_c

    # Add the number if it is the last
    if col == 0:
        nums_for_op.append(int(num_str))
        num_str = ""

    # Add or multiply the found numbers when there is a gap with spaces
    if num_str == "":
        part_res = 0 if ops[current_op_idx] == "+" else 1
        for num in nums_for_op:
            if ops[current_op_idx] == "+":
                part_res += num
            else:
                part_res *= num
        res += part_res
        nums_for_op = []
        current_op_idx -= 1
    else:
        nums_for_op.append(int(num_str))

    # Go to next col
    col -= 1

print(res)
