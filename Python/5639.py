import sys
sys.setrecursionlimit(1000000)


def pretopost(s, e):
    if s >= e:
        return
    root = prefix[s]
    if prefix[e - 1] <= root:
        pretopost(s + 1, e)
        print(root)
        return
    for i in range(s + 1, e):
        if prefix[i] > root:
            tmp = i
            break
    pretopost(s + 1, tmp)
    pretopost(tmp, e)
    print(root)


prefix = []
while True:
    try:
        prefix.append(int(sys.stdin.readline()))
    except:
        break
pretopost(0, len(prefix))
