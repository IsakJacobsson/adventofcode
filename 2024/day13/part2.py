import re

input = open("input.txt").read()

games = input.split('\n\n')

res = 0
for game_i, game in enumerate(games):
    ax, ay, bx, by, px, py = list(map(int, re.findall(r"\d+", game)))

    px, py = px+10000000000000, py+10000000000000
    diff = px-py

    walk_x = walk_y = 0
    a = b = 0
    success = True
    while True:
        if walk_x > 1000000 or walk_y > 1000000:
            success = False
            break
        if walk_x - walk_y == diff:
            break
        if walk_x - walk_y > diff:
            if ay > by:
                walk_x += ax
                walk_y += ay
                a += 1
            else:
                walk_x += bx
                walk_y += by
                b += 1
        else:
            if ax > bx:
                walk_x += ax
                walk_y += ay
                a += 1
            else:
                walk_x += bx
                walk_y += by
                b += 1

    print(a, b)

    px_now = px - walk_x

    walk_x, walk_y = ax, ay
    a2, b2 = 1, 0
    while True:
        if walk_x > 1000000 or walk_y > 1000000:
            success = False
            break
        if walk_x - walk_y == 0:
            break
        if walk_x - walk_y > 0:
            if ay > by:
                walk_x += ax
                walk_y += ay
                a2 += 1
            else:
                walk_x += bx
                walk_y += by
                b2 += 1
        else:
            if ax > bx:
                walk_x += ax
                walk_y += ay
                a2 += 1
            else:
                walk_x += bx
                walk_y += by
                b2 += 1

    if not success or px_now % walk_x != 0:
        continue

    multi = px_now / walk_x

    a = a + multi*a2
    b = b + multi*b2

    print(a,b)

    a -= 99
    b -= 99

    px = px - (ax * a + bx * b)
    py = py - (ay * a + by * b)

    new_a = new_b = 0
    for nbr_a in range(100):
        break_this = False
        for nbr_b in range(100):
            res_x, res_y = nbr_a*ax + nbr_b*bx, nbr_a*ay + nbr_b*by
            if res_x > px or res_y > py:
                continue
            if res_x == px and res_y == py:
                break_this = True
                new_a = nbr_a
                new_b = nbr_b
                break
        if break_this: break

    a += new_a
    b += new_b

    res += 3 * a + b

print(res)