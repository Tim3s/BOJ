import sys

P = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
check = (P[2][0] - P[1][0]) * (P[1][1] - P[0][1]) - (P[2][1] - P[1][1]) * (P[1][0] - P[0][0])
print(0 if check == 0 else int(-check / abs(check)))
