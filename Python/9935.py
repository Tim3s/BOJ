txt = input()
boom = input()
stack = []
length = len(boom)
for char in txt:
    stack.append(char)
    if stack[-1] == boom[-1] and ''.join(stack[-length:]) == boom:
        del stack[-length:]
print(''.join(stack) if stack else "FRULA")
