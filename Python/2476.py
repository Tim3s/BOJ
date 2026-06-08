score = []
for i in range(int(input())):
    a,b,c = map(int, input().split())
    if a == b == c:
        score.append(10000+a*1000)
    elif a == b or b == c:
        score.append(1000 + b * 100)
    elif a == c:
        score.append(1000 + a * 100)
    else:
        score.append(max(a,b,c) * 100)
print(max(score))
