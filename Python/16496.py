from functools import cmp_to_key
input()
def cmp(a, b):
    if len(a) == len(b):
        return 1 if a > b else (0 if a == b else -1)
    if len(a) > len(b):
        return 1 if (a[:len(b)] > b or a[:len(b)] == b and cmp(a[len(b):], b) >= 0) else -1
    return 1 if (a > b[:len(a)] or a == b[:len(a)] and cmp(a, b[len(a):]) > 0) else -1
print(int(''.join(reversed(sorted(input().split(), key=cmp_to_key(cmp))))))