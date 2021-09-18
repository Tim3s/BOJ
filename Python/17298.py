import sys

length = int(sys.stdin.readline())
num = [int(i) for i in sys.stdin.readline().split()]
stack = []
NGE = [0] * length
for i in range(length):
    while len(stack) != 0 and stack[-1][1] < num[i]:
        NGE[stack.pop()[0]] = num[i]
    stack.append([i, num[i]])
while len(stack) != 0:
    NGE[stack.pop()[0]] = -1
print(' '.join([str(i) for i in NGE]))
