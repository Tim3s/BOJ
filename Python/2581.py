M = int(input())
N = int(input())
found = False
mysum = 0
for i in range(M, N + 1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag and i != 1:
        mysum += i
        if not found:
            mymin = i
            found = True
if found:
    print(mysum)
    print(mymin)
else:
    print(-1)
