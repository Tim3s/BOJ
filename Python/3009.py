def findSeq(a, b, c):
    if pita(a, b, c):
        return a, b, c
    if pita(b, a, c):
        return b, a, c
    return c, a, b


def pita(a, b, c):
    return (b[0] - a[0]) * (c[0] - a[0]) + (b[1] - a[1]) * (c[1] - a[1]) == 0


a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
a, b, c = findSeq(a, b, c)
print(b[0] + c[0] - a[0], b[1] + c[1] - a[1])
