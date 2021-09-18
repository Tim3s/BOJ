from itertools import combinations

NM = [int(i) for i in input().split()]
num = input().split()
mymax = 0
mylist = list(combinations(num, 3))
for j in range(len(mylist)):
    mysum = sum([int(k) for k in mylist[j]])
    if mysum > mymax and mysum < NM[1]:
        mymax = mysum
    elif mysum == NM[1]:
        mymax = mysum
        break
print(mymax)
