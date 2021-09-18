import copy
import sys
sys.setrecursionlimit(10 ** 9)


def dfs1(n):
    visited[n] = True
    for v in forward[n]:
        if not visited[v]:
            dfs1(v)
    stack.append(n)


def dfs2(n):
    visited[n] = idx
    for v in backward[n]:
        if visited[v] == -1:
            dfs2(v)


def make(a, b):
    forward[a].append(b)
    backward[b].append(a)


N = int(sys.stdin.readline())
forwar = [[] for _ in range(105)]
backwar = [[] for _ in range(105)]
for _ in range(N):
    investigation = sys.stdin.readline().split()
    card1 = ord(investigation[0][0]) - 64
    card2 = ord(investigation[0][1]) - 64
    player = int(investigation[1])
    cnt = int(investigation[2])
    if player == 2:
        card1 += 26
        card2 += 26
    if cnt == 0:
        forwar[card1].append(-card1)
        forwar[card2].append(-card2)
        backwar[-card1].append(card1)
        backwar[-card2].append(card2)
    elif cnt == 1:
        forwar[card1].append(-card2)
        forwar[-card1].append(card2)
        forwar[card2].append(-card1)
        forwar[-card2].append(card1)
        backwar[-card2].append(card1)
        backwar[card2].append(-card1)
        backwar[-card1].append(card2)
        backwar[card1].append(-card2)
    else:
        forwar[-card1].append(card1)
        forwar[-card2].append(card2)
        backwar[card1].append(-card1)
        backwar[card2].append(-card2)
for i in range(1, 27):
    one = i
    two = i + 26
    forwar[one].append(-two)
    forwar[two].append(-one)
    backwar[-two].append(one)
    backwar[-one].append(two)
cnt = 0
for first in range(1, 27):
    for second in range(first + 1, 27):
        for third in range(second + 1, 27):
            forward = copy.deepcopy(forwar)
            backward = copy.deepcopy(backwar)
            make(first, -first)
            make(first + 26, -first - 26)
            make(second, -second)
            make(second + 26, -second - 26)
            make(third, -third)
            make(third + 26, -third - 26)
            used = [first, second, third]
            for i in range(1, 27):
                if i not in used:
                    one = i
                    two = i + 26
                    make(-one, two)
                    make(-two, one)
            stack = []
            visited = [False] * 105
            for i in range(-52, 0):
                if not visited[i]:
                    dfs1(i)
            for i in range(1, 53):
                if not visited[i]:
                    dfs1(i)
            idx = 0
            visited = [-1] * 105
            while stack:
                cur = stack.pop()
                if visited[cur] == -1:
                    dfs2(cur)
                    idx += 1
            valid = True
            for i in range(1, 53):
                if visited[i] == visited[-i]:
                    valid = False
                    break
            if valid:
                cnt += 1
print(cnt)
