for _ in range(int(input())):
    tmp = input().split()
    res = float(tmp[0])
    for i in range(1, len(tmp)):
        if tmp[i] == "@":
            res *= 3
        elif tmp[i] == "%":
            res += 5
        else:
            res -= 7
    print(f"{res:.2f}")
