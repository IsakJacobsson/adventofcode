def is_ok(values, goal_value, current_value):
    if current_value > goal_value:
        return False
    if not values and goal_value == current_value:
        return True
    if not values:
        return False
    
    value = values[0]
    concat_value = int(str(current_value) + str(value))
    return is_ok(values[1:], goal_value, current_value+value) or is_ok(values[1:], goal_value, current_value*value) or is_ok(values[1:], goal_value, concat_value)

input = open("input.txt").read()

equations = input.split('\n')
res = 0

for equation in equations:
    s = equation.split(': ')
    test_result = int(s[0])
    values = list(map(int, s[1].split(' ')))
    if is_ok(values, test_result, 0):
        res += test_result

print(res)