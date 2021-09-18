import sys


while True:
    num = [int(i) for i in sys.stdin.readline().split()][1:]
    if len(num) == 0:
        break
    s = []
    mymax = 0
    for i in range(len(num)):
        while len(s) != 0 and num[i] < num[s[-1]]:
            height = num[s.pop()]
            if len(s) == 0:
                width = i
            else:
                width = i - s[-1] - 1
            if height * width > mymax:
                mymax = height * width
        s.append(i)
    while len(s) != 0:
        height = num[s.pop()]
        if len(s) == 0:
            width = len(num)
        else:
            width = len(num) - s[-1] - 1
        if height * width > mymax:
            mymax = height * width
    print(mymax)
