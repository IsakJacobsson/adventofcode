import re

input = open("input.txt").read()

games = input.split('\n\n')

res = 0
for game_i, game in enumerate(games):
    ax, ay, bx, by, px, py = list(map(int, re.findall(r"\d+", game)))

    for nbr_a in range(100):
        break_this = False
        for nbr_b in range(100):
            res_x, res_y = nbr_a*ax + nbr_b*bx, nbr_a*ay + nbr_b*by
            if res_x > px or res_y > py:
                break
            if res_x == px and res_y == py:
                res += nbr_a*3 + nbr_b
                break_this = True
                break
        if break_this: break

print(res)