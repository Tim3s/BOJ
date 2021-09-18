ln = int(input())
for nothing in range(ln):
    num = [int(i) for i in input().split()]
    if num[0] == num[3] and num[1] == num[4]:
        if num[2] == num[5]:
            print(-1)
        else:
            print(0)
    else:
        distance = (num[3] - num[0]) ** 2 + (num[4] - num[1]) ** 2
        maxradius = (num[2] + num[5]) ** 2
        minradius = (num[2] - num[5]) ** 2
        if distance > maxradius or distance < minradius:
            print(0)
        elif distance == maxradius or distance == minradius:
            print(1)
        else:
            print(2)
