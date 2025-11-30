lines = open("input.txt").readlines()

res = 0

for line in lines:
    increasing = True
    line = line.replace('\n', '')
    numbers = list(map(int, line.split(' ')))
    print(numbers)
    safe = True
    for i, number in enumerate(numbers):
        if i == 0: continue
        if i == 1:
            increasing = number > numbers[i-1]
        
        if increasing and number < numbers[i-1]:
            safe = False
            break

        if not increasing and number > numbers[i-1]:
            safe = False
            break

        if abs(number-numbers[i-1]) > 3:
            safe = False
            break

        if number == numbers[i-1]:
            safe = False
            break
    
    if safe:
        res += 1

print(res)

    

