#ax, ay, bx, by = 19, 50, 58, 35 
ax, ay, bx, by = 96, 77, 74, 11

walk_x, walk_y = ax, ay
a, b = 1, 0
success = True
while True:
    print(walk_x, walk_y)
    if walk_x > 10000 or walk_y > 100000:
        success = False
        break
    if walk_x - walk_y == 0:
        print(a, b)
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