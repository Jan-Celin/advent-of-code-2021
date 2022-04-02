from math import floor
polje = []
maxx = 0
maxy = 0
##for i in range(846):
##    x, y = map(int, input().split(","))
##    if x > maxx:
##        maxx = x
##    if y > maxy:
##        maxy = y
##print(maxx, maxy)

##polje = [['.' for i in range(1311)] for i in range(894)]
##for i in range(846):
##    x, y = map(int, input().split(","))
##    polje[y][x] = '#'
##
##br = 0
##for i in range(894):
##    for j in range(656):
##        if polje[i][j] == '#' or polje[i][893-j] == '#':
##            br += 1
##print(br)

##polje = [['.' for i in range(1311)] for j in range(894)]
##for i in range(846):
##    x, y = map(int, input().split(","))
##    polje[y][x] = '#'
##
##x = 1310
##y = 893
##
##for ii in range(12):
##    a = input()
##    if 'x' in a:
##        locx = a.index('=')
##        ox = x
##        x = int(a[locx+1:])
##        for i in range(y + 1):
##            for j in range(x + 1):
##                if polje[i][ox - j] == '#':
##                    polje[i][j] = '#'
##    else:
##        locy = a.index('=')
##        oy = y
##        y = int(a[locy+1:])
##        for i in range(y + 1):
##            for j in range(x + 1):
##                if polje[oy - i][j] == '#':
##                    polje[i][j] = '#'
##    print(x, y)
##    if ii < 8:
##        continue
##    for j in range(y):
##        s = ''
##        for k in polje[j][:x]:
##            s += k
##        print(s)


polje = [['.' for i in range(1311)] for j in range(894)]
for i in range(846):
    x, y = map(int, input().split(","))
    polje[y][x] = '#'

empty = input()
##polje = []
##maxx = 0
##maxy = 0
##for i in range(846):
##    x, y = map(int, input().split(","))
##    if x > maxx:
##        maxx = x
##    if y > maxy:
##        maxy = y
##print(maxx, maxy)

x = 1310
y = 893

for i in range(12):
    instruction = input()
    equals_location = instruction.index("=")
    if 'x' in instruction:
        fold_location = int(instruction[equals_location+1:])
        if fold_location == x/2:
            for j, red in enumerate(polje):
                for k, element in enumerate(red[1:fold_location]):
                    if polje[j][x-k] == "#":
                        polje[j][k] = "#"
        elif fold_location < x/2:
            for j, red in enumerate(polje):
                for k, element in enumerate(red[:fold_location+1]):
                    if polje[j][x-k-1] == "#":
                        polje[j][k] = "#"
        elif fold_location > x/2:
            for j, red in enumerate(polje):
                for k, element in enumerate(red[2:fold_location+1]):
                    if polje[j][x-k+1] == "#":
                        polje[j][k] = "#"
        x = fold_location
        
    if 'y' in instruction:
        fold_location = int(instruction[equals_location+1:])
        if fold_location == y/2: #nikad
            for j, red in enumerate(polje):
                for k, element in enumerate(red[1:fold_location]):
                    if polje[j][y-k] == "#":
                        polje[j][k] = "#"
        elif fold_location < y/2:
            for j, red in enumerate(polje[:fold_location+1]):
                for k, element in enumerate(red):
                    if polje[j][y-k-1] == "#":
                        polje[j][k] = "#"
        elif fold_location > y/2:
            for j, red in enumerate(polje[2:fold_location+1]):
                for k, element in enumerate(red):
                    if polje[j][y-k+1] == "#":
                        polje[j][k] = "#"
        y = fold_location

for row in polje[:40]:
    s = ''
    for j in row[:40]:
        s += j
    print(s)


























































