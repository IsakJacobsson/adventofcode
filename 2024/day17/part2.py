import sys
import time

start_time = time.time()

bin8 = ['000','001', '010', '011', '100', '101', '110', '111']

program = [2,4,1,1,7,5,1,5,0,3,4,3,5,5,3,0]

def req(a_start, i):
    ok_ext = []
    for b in bin8:
        a_reg = int(a_start + b, 2)
        b_reg = 0
        c_reg = 0
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
                res = a_reg >> combo
                a_reg = res
            elif opcode == 1:
                res = b_reg ^ literal
                b_reg = res
            elif opcode == 2:
                res = combo & 0b111
                b_reg = res
            elif opcode == 3:
                if a_reg != 0:
                    pc = literal
                    continue
            elif opcode == 4:
                res = b_reg ^ c_reg
                b_reg = res
            elif opcode == 5:
                res = combo & 0b111
                out.append(res)
            elif opcode == 6:
                res = a_reg >> combo
                b_reg = res
            elif opcode == 7:
                res = a_reg >> combo
                c_reg = res

            pc += 2

        if out[0] == program[i]:
            ok_ext.append(b)
            if i == 0: return a_start + b

    for b in ok_ext:
        res = req(a_start + b, i-1)
        if res:
            return res
    
    return ''

res = req('', 15)

print(int(res, 2))

end_time = time.time()
print("Time: ", end_time-start_time)
        
