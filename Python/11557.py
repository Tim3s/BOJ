for t in range(int(input())):
    alcohol = []
    for n in range(int(input())):
        alcohol.append(input().split())
    print(sorted(alcohol, key=lambda x: int(x[1]), reverse=True)[0][0])