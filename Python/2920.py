num = [int(i) for i in input().split()]
if num[0] == 1:
    flag = True
    for i in range(1, 8):
        if num[i] != i + 1:
            flag = False
            break
    if flag:
        print("ascending")
    else:
        print("mixed")
elif num[0] == 8:
    flag = True
    for i in range(1, 8):
        if num[i] != 8 - i:
            flag = False
            break
    if flag:
        print("descending")
    else:
        print("mixed")
else:
    print("mixed")
