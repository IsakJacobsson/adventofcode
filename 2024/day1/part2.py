import time

start_time = time.time()
with open("input.txt") as file:
    lines = file.readlines()

    list1 = []
    list2 = []
    for line in lines:
        ids = line.split('   ')
        id1, id2 = map(int, ids)
        list1.append(id1)
        list2.append(id2)

    my_dict = {}
    res = 0
    for id2 in list2:
        if id2 in my_dict:
            my_dict[id2] += 1
        else:
            my_dict[id2] = 1
        
    for id1 in list1:
        res += id1 * my_dict.get(id1, 0)

print(res)

end_time = time.time()
print("Time: ", end_time-start_time)