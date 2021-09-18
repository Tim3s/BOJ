N, r, c = map(int, input().split())
res = 0
cur = 2
while r > 0:
    if r % 2:
        res += cur
    cur *= 4
    r //= 2
cur = 1
while c > 0:
    if c % 2:
        res += cur
    cur *= 4
    c //= 2
print(res)
