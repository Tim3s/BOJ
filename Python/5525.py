N = int(input())
M = int(input())
S = input()
res = 0
P = 0
i = 1
while i < M - 1:
    if S[i - 1] == 'I' and S[i] == 'O' and S[i + 1] == 'I':
        P += 1
        i += 1
        if P == N:
            P -= 1
            res += 1
    else:
        P = 0
    i += 1
print(res)
