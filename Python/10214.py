for _ in range(int(input())):
    win = 0
    for _ in range(9):
        Y, K = map(int, input().split())
        win += Y-K
    if win>0:
        print("Yonsei")
    elif win<0:
        print("Korea")
    else:
        print("Draw")
        