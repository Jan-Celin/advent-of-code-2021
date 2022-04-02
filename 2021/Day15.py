R = 500
S = 500
  
def minCost(cost, m, n):

    tc = [[0 for x in range(S)] for x in range(R)]
  
    for i in range(1, m + 1):
        tc[i][0] = tc[i-1][0] + cost[i][0]
  
    for j in range(1, n + 1):
        tc[0][j] = tc[0][j-1] + cost[0][j]
  
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            tc[i][j] = min(tc[i-1][j], tc[i][j-1]) + cost[i][j]
  
    return tc[m][n]


mat = []
for i in range(100):
    row = input()
    mat_row = []
    for j in row:
        mat_row.append(int(j))
        
    mat.append(mat_row)

new_mat = [[0 for j in range(500)] for i in range(500)]
for i in range(500):
    for j in range(500):
        if mat[i%100][j%100] + (i // 100  + j // 100) > 9:
            new_mat[i][j] = mat[i%100][j%100] + (i // 100  + j // 100) - 9
        else:
            new_mat[i][j] = mat[i%100][j%100] + (i // 100  + j // 100)

            
print(new_mat[499][499])
print(minCost(new_mat, 499, 499))











