txt = input()
stack = ['(']
for i in range(len(txt)):
    if txt[i].isalpha():
        print(txt[i], end='')
    elif txt[i] == '(':
        stack.append('(')
    elif txt[i] == ')':
        while stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()
    elif txt[i] == '*' or txt[i] == '/':
        while stack[-1] != '(' and stack[-1] != '-' and stack[-1] != '+':
            print(stack.pop(), end='')
        stack.append(txt[i])
    else:
        while stack[-1] != '(':
            print(stack.pop(), end='')
        stack.append(txt[i])
while stack[-1] != '(':
    print(stack.pop(), end='')
