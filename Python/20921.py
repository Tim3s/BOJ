N, K = map(int, input().split())
left = 1
right = N
for i in range(N - 1, -1, -1):
    if K >= i:
        print(right, end=' ')
        K -= i
        right -= 1
    else:
        print(left, end=' ')
        left += 1
