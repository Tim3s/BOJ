ln = int(input())
n = 0
for nothing in range(ln):
    index = 0
    cur = input()
    group = True
    while index < len(cur):
        curc = cur[index]
        index += 1
        while index <= cur.rindex(curc):
            if cur[index] != curc:
                group = False
                break
            index += 1
        if not group:
            break
    if group:
        n += 1
print(n)
