import sys
loop = int(sys.stdin.readline())
stack = []
result = ""
num = 1
for i in range(loop):
    cur = int(sys.stdin.readline())
    while len(stack) == 0 or stack[-1] < cur:
        stack.append(num)
        result += "+\n"
        num += 1
    if stack[-1] != cur:
        print("NO")
        sys.exit(0)
    stack.pop()
    result += "-\n"
print(result)
