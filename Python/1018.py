NM = [int(i) for i in input().split()]
mylist = []
mymin = 64
for i in range(NM[0]):
    mylist.append(input())
for i in range(NM[0] - 7):
    for j in range(NM[1] - 7):
        mysum = 0
        for k in range(8):
            for l in range(8):
                if(i + j + k + l) % 2 == 0 and mylist[i + k][j + l] == 'B':
                    mysum += 1
                elif(i + j + k + l) % 2 == 1 and mylist[i + k][j + l] == 'W':
                    mysum += 1
        mymin = min(mymin, mysum, 64 - mysum)
print(mymin)
