import sys

s = sys.stdin.readline().rstrip()
while s != '.':
    newidx = [0] * len(s)
    idx = 0
    for i in range(1, len(s)):
        while idx > 0 and s[i] != s[idx]:
            idx = newidx[idx - 1]
        if s[idx] == s[i]:
            idx += 1
            newidx[i] = idx
    print(1 if len(s) % (len(s) - newidx[-1]) else len(s) // (len(s) - newidx[-1]))
    s = sys.stdin.readline().rstrip()
