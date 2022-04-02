count1 = 0
count2 = 0

def find_sol(p, s1, s2, pos1, pos2, roll, uni):
    global count1
    global count2
    if p == 1:
        pos1 += roll
        if pos1 > 10:
            pos1 -= 10
        s1 += pos1
        if s1 >= 21:
            count1 += uni
        else:
            find_sol(2, s1, s2, pos1, pos2, 1, uni+1)
            find_sol(2, s1, s2, pos1, pos2, 2, uni+1)
            find_sol(2, s1, s2, pos1, pos2, 3, uni+1)
    if p == 2:
        pos2 += roll
        if pos2 > 10:
            pos2 -= 10
        s2 += pos2
        if s2 >= 21:
            count2 += uni
        else:
            find_sol(1, s1, s2, pos1, pos2, 1, uni+1)
            find_sol(1, s1, s2, pos1, pos2, 2, uni+1)
            find_sol(1, s1, s2, pos1, pos2, 3, uni+1)

find_sol(1, 0, 0, 10, 6, 1, 1)
find_sol(1, 0, 0, 10, 6, 2, 1)
find_sol(1, 0, 0, 10, 6, 3, 1)
print(count1, count2)
