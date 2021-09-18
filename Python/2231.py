N = int(input())
make = 0
for i in range(int(N / 2), N):
    mysum = i
    j = i
    while j > 0:
        mysum += j % 10
        j = int(j / 10)
    if mysum == N:
        make = i
        break
print(make)
