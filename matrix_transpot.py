a = [[1, 1, 1], [2, 2, 2]]
b = [[0, 0, 0], [0, 0, 0]]
for i in range(len(a)):
    for j in range(len(a)):
        b[i][j] = a[j][i]
for i in b:
    print(i)
