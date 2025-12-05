with open("input.txt", "r") as f:
    s = f.read().strip()

res = 0

# for row in s.split("\n"):
#     nums = [int(i) for i in row]
#     first = 0
#     second = 0
#     for i in nums[:-1]:
#         if i > first:
#             first = i
#             second = nums[-1]
#         elif i > second:
#             second = i
#     res += first * 10 + second

for row in s.split("\n"):
    highest = []
    nums = [int(i) for i in row]
    startidx = 0
    for i in range(-11, 0, 1):
        next = 0
        next_startidx = 0
        for idx, num in enumerate(nums[startidx:i]):
            if num > next:
                next = num
                next_startidx = idx + 1
        highest.append(next)
        startidx += next_startidx

    next = 0
    for num in nums[startidx:]:
        if num > next:
            next = num
    highest.append(next)

    t = 0
    highest.reverse()
    for idx, num in enumerate(highest):
        t += num * 10**idx

    res += t

print(res)
