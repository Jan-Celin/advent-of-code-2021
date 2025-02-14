def increase_by_1(matrix):
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            matrix[i][j] += 1
    return matrix

def flash(matrix, y, x):
    if y == 0 and x == 0:
        matrix[y+1][x] += 1
        matrix[y][x+1] += 1
        matrix[y+1][x+1] += 1
    elif y == 9 and x == 9:
        matrix[y-1][x] += 1
        matrix[y][x-1] += 1
        matrix[y-1][x-1] += 1
    elif y == 0 and x == 9:
        matrix[y+1][x] += 1
        matrix[y][x-1] += 1
        matrix[y+1][x-1] += 1
    elif y == 9 and x == 0:
        matrix[y-1][x] += 1
        matrix[y][x+1] += 1
        matrix[y-1][x+1] += 1
    elif y == 0:
        matrix[y][x-1] += 1
        matrix[y][x+1] += 1
        matrix[y+1][x] += 1
        matrix[y+1][x-1] += 1
        matrix[y+1][x+1] += 1
    elif x == 0:
        matrix[y+1][x] += 1
        matrix[y-1][x] += 1
        matrix[y][x+1] += 1
        matrix[y-1][x+1] += 1
        matrix[y+1][x+1] += 1
    elif y == 9:
        matrix[y][x-1] += 1
        matrix[y][x+1] += 1
        matrix[y-1][x] += 1
        matrix[y-1][x-1] += 1
        matrix[y-1][x+1] += 1
    elif x == 9:
        matrix[y+1][x] += 1
        matrix[y-1][x] += 1
        matrix[y][x-1] += 1
        matrix[y-1][x-1] += 1
        matrix[y+1][x-1] += 1
    else:
        matrix[y][x-1] += 1
        matrix[y][x+1] += 1
        matrix[y-1][x] += 1
        matrix[y+1][x] += 1
        matrix[y-1][x-1] += 1
        matrix[y-1][x+1] += 1
        matrix[y+1][x-1] += 1
        matrix[y+1][x+1] += 1
    for I, r in enumerate(matrix):
        for J, e in enumerate(r):
            if e > 10 and e < 1000:
                matrix[I][J] = 10
    return matrix
mat = []
for i in range(10):
    row = input()
    row_list = []
    for j in row:
        row_list.append(int(j))
    mat.append(row_list)

count = 0
for step in range(1000):
    countstep = 0
    mat = increase_by_1(mat)
    while True:
        nines = []
        for i, row in enumerate(mat):
            for j, element in enumerate(row):
                if element == 10:
                    nines.append([i, j])
        for i in nines:
            mat = flash(mat, i[0], i[1])
            mat[i[0]][i[1]] = 100000
        end = 1
        for i, row in enumerate(mat):
            for j, element in enumerate(row):
                if element == 10:
                    end = 0
        if end:
            break
    for i, row in enumerate(mat):
        for j, element in enumerate(row):
            if element >= 10:
                mat[i][j] = 0
                countstep += 1
                count += 1
    if countstep == 100:
        break
print(step)





























































        
