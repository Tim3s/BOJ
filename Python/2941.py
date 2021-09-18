mystr = input()
n = 0
ntp = 0
for i in range(len(mystr)):
    if ntp == 0:
        if mystr[i] == 'c':
            if i + 1 < len(mystr) and (mystr[i + 1] == '=' or mystr[i + 1] == '-'):
                ntp = 1
            n += 1
        elif mystr[i] == 'd':
            if i + 1 < len(mystr) and mystr[i + 1] == '-':
                ntp = 1
            elif i + 2 < len(mystr) and mystr[i + 1] == 'z' and mystr[i + 2] == '=':
                ntp = 2
            n += 1
        elif mystr[i] == 'l' or mystr[i] == 'n':
            if i + 1 < len(mystr) and mystr[i + 1] == 'j':
                ntp = 1
            n += 1
        elif mystr[i] == 's' or mystr[i] == 'z':
            if i + 1 < len(mystr) and mystr[i + 1] == '=':
                ntp = 1
            n += 1
        else:
            n += 1
    else:
        ntp -= 1
print(n)