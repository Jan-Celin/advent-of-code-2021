n = 1000
depth = 0
dist = 0
aim = 0
for i in range(n):
    com, x = map(str, input().split())
    if com == 'up':
        aim -= int(x)
    elif com == 'down':
        aim += int(x)
    else:
        dist += int(x)
        depth += aim * int(x)

print(dist*depth)
