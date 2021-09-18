N = int(input())
isprime = [True] * (N + 1)
primelist = []
for i in range(2, N + 1):
    if isprime[i]:
        primelist.append(i)
        for j in range(i * i, N + 1, i):
            isprime[j] = False
i = j = 0
cnt = 0
tmpsum = 0
while tmpsum >= N or j != len(primelist):
    if tmpsum < N:
        tmpsum += primelist[j]
        j += 1
        continue
    if tmpsum == N:
        cnt += 1
    tmpsum -= primelist[i]
    i += 1
print(cnt)
