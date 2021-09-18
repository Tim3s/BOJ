A = input()
B = input()
Alen = len(A)
Blen = len(B)
matrix = [[0] * Blen for i in range(Alen)]
if A[0] == B[0]:
    matrix[0][0] = 1
for i in range(1, Alen):
    if A[i] == B[0]:
        matrix[i][0] = 1
    else:
        matrix[i][0] = matrix[i - 1][0]
for i in range(1, Blen):
    if A[0] == B[i]:
        matrix[0][i] = 1
    else:
        matrix[0][i] = matrix[0][i - 1]
for i in range(1, Alen):
    for j in range(1, Blen):
        if A[i] != B[j]:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
        else:
            matrix[i][j] = matrix[i - 1][j - 1] + 1
cur = matrix[Alen - 1][Blen - 1]
res = ''
x, y = Alen, Blen
while cur:
    done = False
    for i in range(cur - 1, x):
        for j in range(cur - 1, y):
            if matrix[i][j] == cur:
                res = A[i] + res
                x, y = i, j
                done = True
                break
        if done:
            break
    cur -= 1
print(res)
