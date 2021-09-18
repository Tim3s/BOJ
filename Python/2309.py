num = sorted([int(input()) for _ in range(9)])
tmp = sum(num)
done = False
for i in range(8):
    for j in range(i + 1, 9):
        if tmp - num[i] - num[j] == 100:
            todelete = [i, j]
            done = True
            break
    if done:
        break
del num[todelete[1]]
del num[todelete[0]]
print('\n'.join(list(map(str, num))))
