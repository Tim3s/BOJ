import sys
from fractions import Fraction

N = int(sys.stdin.readline())
formula = sys.stdin.readline().split()
used = [False] * len(formula)
u = list(map(int, sys.stdin.readline().split()))
v = 0
for i in range(0, len(formula), 2):
    formula[i] = Fraction(formula[i])
for calc in u:
    v = v ^ calc
    # print('v:', v)
    former = v * 2 - 2
    # print(former)
    while used[former]:
        # print('used:', former)
        former -= 2
    latter = v * 2
    used[latter] = True
    op = v * 2 - 1
    if formula[op] == '+':
        formula[former] += formula[latter]
    elif formula[op] == '-':
        formula[former] -= formula[latter]
    elif formula[op] == '*':
        formula[former] *= formula[latter]
    else:
        formula[former] /= formula[latter]
    print((formula[former].numerator * pow(formula[former].denominator, 10 ** 9 + 6, 10 ** 9 + 7)) % (10 ** 9 + 7))
