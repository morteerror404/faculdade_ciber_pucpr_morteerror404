matrix = [[0, 0, 0, 0], [0, 0, 0, 0],[0, 0, 0, 0]]
a = 0

for i in range(4):
    a = i + 1
    matrix[0][i] = a
for j in range (4):
    b = j + 5
    matrix[1][j] = b
for k in range (4):
    c = k + 9
    matrix[2][k] = c
        
for p in range (3):
    print(matrix[p])
    
for h in range (3):
    for z in range (4):
        matrix[h][z] = matrix[h][z] * 2

print()
for p in range(3):
    print(matrix[p])
