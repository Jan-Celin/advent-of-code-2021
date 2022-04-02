lines = 137
columns = 139
mat = []
for i in range(lines):
    row = input()
    row_list = []
    for element in row:
        row_list.append(element)
    mat.append(row_list)

count = 0
nmat = [[0 for i in range(columns)] for j in range(lines)]
while True:
    for i, row in enumerate(mat):
        for j, element in enumerate(row):
            nmat[i][j] = element
    count += 1
    moved = 0
    for i, row in enumerate(mat):
        for j, element in enumerate(row):
            if element == '>':
                
                if j == columns - 1:
                    if mat[i][0] == '.':
                        moved = 1
                        nmat[i][0] = '>'
                        nmat[i][j] = '.'
                else:
                    if mat[i][j+1] == '.':
                        moved = 1
                        nmat[i][j+1] = '>'
                        nmat[i][j] = '.'
                    
    for i, row in enumerate(nmat):
        for j, element in enumerate(row):
            mat[i][j] = element
            
    for i, row in enumerate(mat):
        for j, element in enumerate(row):
            if element == 'v':
                if i == lines - 1:
                    if mat[0][j] == '.':
                        moved = 1
                        nmat[0][j] = 'v'
                        nmat[i][j] = '.'
                else:
                    if mat[i+1][j] == '.':
                        moved = 1
                        nmat[i+1][j] = 'v'
                        nmat[i][j] = '.'
                    
    for i, row in enumerate(nmat):
        for j, element in enumerate(row):
            mat[i][j] = element
            
    if not moved:
        print(count)
        break



                    
