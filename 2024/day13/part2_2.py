import re

input = open("input.txt").read()

games = input.split('\n\n')

res = 0
for game_i, game in enumerate(games):
    print(game_i)
    ax, ay, bx, by, px, py = list(map(int, re.findall(r"\d+", game)))

    endpx = 10000000000000 + px
    endpy = 10000000000000 + py

    walk_x, walk_y = ax, ay
    a, b = 1, 0
    success = True
    while True:
        if walk_x > 10000 or walk_y > 100000:
            success = False
            break
        if walk_x - walk_y == 0:
            break
        if walk_x - walk_y > 0:
            if ax < ay:
                walk_x += ax
                walk_y += ay
                a += 1
            else:
                walk_x += bx
                walk_y += by
                b += 1
        else:
            if ax > ay:
                walk_x += ax
                walk_y += ay
                a += 1
            else:
                walk_x += bx
                walk_y += by
                b += 1
    if not success:
        print(game_i, "he")
        continue
    

    multi = 10000000000000 // walk_x


    a = multi*a-200
    b = multi*b-200

    px, py = endpx - (a*ax + b*bx), endpy - (a*ay + b*by)

    new_a = new_b = 0
    for nbr_a in range(10000):
        break_this = False
        for nbr_b in range(10000):
            res_x, res_y = nbr_a*ax + nbr_b*bx, nbr_a*ay + nbr_b*by
            if res_x > px or res_y > py:
                break
            if res_x == px and res_y == py:
                break_this = True
                new_a = nbr_a
                new_b = nbr_b
                break
        if break_this: break

    if new_a == 0 and new_b == 0:
        continue

    a += new_a
    b += new_b
    res += 3 * a + b

print(res)