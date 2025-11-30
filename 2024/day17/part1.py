import sys


a_reg = 56256477
b_reg = 0
c_reg = 0

program = [2,4,1,1,7,5,1,5,0,3,4,3,5,5,3,0]

pc = 0
out = []

while pc < len(program):
    opcode = program[pc]
    literal = program[pc+1]
    if literal <= 3:
        combo = literal
    elif literal == 4:
        combo = a_reg
    elif literal == 5:
        combo = b_reg
    elif literal == 6:
        combo = c_reg
    else:
        print("Fail: Combo operand with literal value", literal)
        sys.exit(1)

    if opcode == 0:
        res = a_reg // (2**combo)
        a_reg = res
    elif opcode == 1:
        res = b_reg ^ literal
        b_reg = res
    elif opcode == 2:
        res = combo % 8
        b_reg = res
    elif opcode == 3:
        if a_reg != 0:
            pc = literal
            continue
    elif opcode == 4:
        res = b_reg ^ c_reg
        b_reg = res
    elif opcode == 5:
        res = combo % 8
        out.append(str(res))
    elif opcode == 6:
        res = a_reg // (2**combo)
        b_reg = res
    elif opcode == 7:
        res = a_reg // (2**combo)
        c_reg = res

    pc += 2

print(','.join(out))
