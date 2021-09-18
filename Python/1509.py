txt = list(input())
N = len(txt)
palindrome = [[False] * N for _ in range(N)]
for i in range(N):
    palindrome[i][i] = True
    left = i - 1
    right = i + 1
    while 0 <= left and right < N:
        if txt[left] == txt[right]:
            palindrome[left][right] = True
            left -= 1
            right += 1
            continue
        break
    left = i
    right = i + 1
    while 0 <= left and right < N:
        if txt[left] == txt[right]:
            palindrome[left][right] = True
            left -= 1
            right += 1
            continue
        break
memo = [2500] * N
memo[0] = 1
for i in range(1, N):
    if palindrome[0][i]:
        memo[i] = 1
for i in range(1, N):
    for j in range(i, N):
        if palindrome[i][j] and memo[j] > memo[i - 1] + 1:
            memo[j] = memo[i - 1] + 1
print(memo[-1])
