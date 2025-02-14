mat = []
for i in range(100):
    row = input()
    int_row = []
    for j in range(100):
        int_row.append(int(row[j]))
    mat.append(int_row)

bio = [[0 for i in range(100)] for j in range(100)]
basin_sizes = []
for i, row in enumerate(mat):
    for j, element in enumerate(row):
        if bio[i][j] or mat[i][j] == 9:
            continue
        basin_size = 0
        start = [i, j]
        q = [[i,j]]
        while q:
            curr = q[0]
            q.remove(curr)
            curri = curr[0]
            currj = curr[1]
            if bio[curri][currj] or mat[curri][currj] == 9:
                continue
            basin_size += 1
            bio[curri][currj] = 1
            if curri+1 < 100:
                q.append([curri+1, currj])
            if curri-1 >= 0:
                q.append([curri-1, currj])
            if currj+1 < 100:
                q.append([curri, currj+1])
            if currj-1 >= 0:
                q.append([curri, currj-1])
        basin_sizes.append(basin_size)
basin_sizes.sort(reverse=True)
print(basin_sizes[:3])
