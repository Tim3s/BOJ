num = int(input())
if num == 4 or num == 7:
    print(-1)
else:
    b = int(num / 5)
    while (num - b * 5) % 3 != 0:
        b -= 1
    print(int(b + (num - b * 5) / 3))
