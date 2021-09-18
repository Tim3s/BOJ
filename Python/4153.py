while True:
    num = [int(i) for i in input().split()]
    if num[0] == 0 and num[1] == 0 and num[2] == 0:
        break
    if (max(num) ** 2 - min(num) ** 2) ** 0.5 in num:
        print('right')
    else:
        print('wrong')
