def make(cnt, cur):
    if cnt == M == 1:
        print('\n'.join(map(str, num)))
    elif cnt == 1:
        for i in range(N):
            make(2, str(num[i]))
    elif cnt == M:
        for i in range(N):
            print(cur + ' ' + str(num[i]))
    else:
        cnt += 1
        for i in range(N):
            make(cnt, cur + ' ' + str(num[i]))


N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
make(1, '')
