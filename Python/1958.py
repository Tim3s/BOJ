import sys
A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()
C = sys.stdin.readline().rstrip()
Alen = len(A)
Blen = len(B)
Clen = len(C)
matrix = [[[0] * (Clen + 1) for _ in range(Blen + 1)] for _ in range(Alen + 1)]
for i in range(Alen):
    for j in range(Blen):
        for k in range(Clen):
            if A[i] == B[j] == C[k]:
                matrix[i][j][k] = matrix[i-1][j-1][k-1] + 1
            else:
                matrix[i][j][k] = max(matrix[i-1][j][k], matrix[i][j-1][k], matrix[i][j][k-1])
print(matrix[Alen-1][Blen-1][Clen-1])
