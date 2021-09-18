def mul(a, b):
    return [[sum([a[i][k] * b[k][j] for k in range(8)]) % 1000000007 for j in range(8)] for i in range(8)]


D = int(input())
univ = [[0] * 8 for _ in range(8)]
univ[0][1] = univ[1][0] = 1
univ[0][7] = univ[7][0] = 1
univ[1][2] = univ[2][1] = 1
univ[1][7] = univ[7][1] = 1
univ[2][3] = univ[3][2] = 1
univ[2][6] = univ[6][2] = 1
univ[2][7] = univ[7][2] = 1
univ[3][4] = univ[4][3] = 1
univ[3][6] = univ[6][3] = 1
univ[4][5] = univ[5][4] = 1
univ[5][6] = univ[6][5] = 1
univ[6][7] = univ[7][6] = 1
ans = [[0] * 8 for _ in range(8)]
for i in range(8):
    ans[i][i] = 1
while D > 0:
    if D % 2:
        ans = mul(ans, univ)
    univ = mul(univ, univ)
    D //= 2
print(ans[0][0])
