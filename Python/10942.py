import sys

N = int(sys.stdin.readline())
num = [0] + list(map(int, sys.stdin.readline().split()))
palindrome = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    palindrome[i][i] = 1
    left = i - 1
    right = i + 1
    while 0 < left and right <= N:
        if num[left] == num[right]:
            palindrome[left][right] = 1
            left -= 1
            right += 1
            continue
        break
    left = i
    right = i + 1
    while 0 < left and right <= N:
        if num[left] == num[right]:
            palindrome[left][right] = 1
            left -= 1
            right += 1
            continue
        break
M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(palindrome[a][b])
