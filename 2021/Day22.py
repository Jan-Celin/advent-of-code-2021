grid = [[[0 for i in range(-50, 51)] for j in range(-50, 51)] for k in range(-50, 51)]
N_instructions = 420

for T in range(N_instructions):
    if T >= 20:
        break
    state_change, koordinates = map(str, input().split())
    x, y, z = map(str, koordinates.split(','))
    x = x[2:]
    y = y[2:]
    z = z[2:]
    x1, x2 = map(int, x.split('..'))
    y1, y2 = map(int, y.split('..'))
    z1, z2 = map(int, z.split('..'))

    if state_change == 'on':
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                for k in range(z1, z2+1):
                    grid[i][j][k] = 1
    if state_change == 'off':
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                for k in range(z1, z2+1):
                    grid[i][j][k] = 0

count = 0
for i in grid:
    for j in i:
        for k in j:
            if k == 1:
                count += 1
print(count)
