def compress(start):
    cnt = 0
    for i in range(start, len(S)):
        if S[i] == '(' and not visited[i]:
            visited[i] = True
            cnt -= 1
            cnt += int(S[i - 1]) * compress(i + 1)
        elif S[i] == ')' and not visited[i]:
            visited[i] = True
            return cnt
        elif not visited[i]:
            visited[i] = True
            cnt += 1
    return cnt


S = input()
visited = [False] * 50
print(compress(0))
