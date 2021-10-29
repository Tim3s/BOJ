N = int(input())
left = 1
right = N - 1
print(N, end=' ')
while left < right:
    print(left, right, end=' ')
    left += 1
    right -= 1
if left == right:
    print(left)
