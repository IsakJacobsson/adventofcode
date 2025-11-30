with open("input.txt") as file:
    lines = file.readlines()

    list1 = []
    list2 = []
    for line in lines:
        ids = line.split('   ')
        id1, id2 = map(int, ids)
        list1.append(id1)
        list2.append(id2)

    list1.sort()
    list2.sort()

    res = 0
    for id1, id2 in zip(list1, list2):
        res += abs(id1-id2)

print(res)