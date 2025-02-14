mat = [[0 for i in range(1000)] for j in range(1000)]

for i in range(500):
    line_begin, line_end = map(str, input().split(" -> "))

    x1, y1 = map(int, line_begin.split(","))
    x2, y2 = map(int, line_end.split(","))
        
    if x1 == x2:
        for j in range(min(y1, y2), max(y1, y2)+1):
            mat[j][x1] += 1
    elif y1 == y2:
        for j in range(min(x1, x2), max(x1, x2)+1):
            mat[y1][j] += 1
    else:
        x = abs(x1-x2)
        if x1 < x2 and y1 < y2:
            j = y1
            k = x1
            while (k,j) != (x2,y2):
                mat[j][k] += 1
                j += 1
                k += 1
            mat[y2][x2] += 1
        elif x1 > x2 and y1 < y2:
            j = y1
            k = x1
            while (k,j) != (x2,y2):
                mat[j][k] += 1
                j += 1
                k -= 1
            mat[y2][x2] += 1
        elif x1 > x2 and y1 > y2:
            j = y1
            k = x1
            while (k,j) != (x2,y2):    
                mat[j][k] += 1
                j -= 1
                k -= 1
            mat[y2][x2] += 1
        elif x1 < x2 and y1 > y2:
            j = y1
            k = x1
            while (k,j) != (x2,y2):  
                mat[j][k] += 1
                j -= 1
                k += 1
            mat[y2][x2] += 1
count = 0
for row in mat:
    for element in row:
        if element >= 2:
            count += 1

print(count)
