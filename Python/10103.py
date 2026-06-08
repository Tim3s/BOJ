scores = [100,100]
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a>b:
        scores[1] -= a
    elif a<b:
        scores[0] -= b
print(scores[0])
print(scores[1])