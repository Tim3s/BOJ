import sys
N = int(sys.stdin.readline())
l = sys.stdin.readline().split()
A = l[0]
B = int(l[1])
for _ in range(N-1):
    l = sys.stdin.readline().split()
    if int(l[1]) > B:
        B = int(l[1])
        A = l[0]
        continue
    if int(l[1]) == B:
        A = min(A, l[0])
print(A)
