import sys
import math

A, B = sys.stdin.readline().split()
A = bin(int(A) - 1)[2:][::-1]
B = bin(int(B))[2:][::-1]
Alen = len(A)
Blen = len(B)
Asum = 0
one = 0
for i in range(Alen):
    if A[i] == '1':
        one += 1
for i in range(Alen):
    if A[i] == '1':
        Asum += 1
        one -= 1
        if i != 0:
            Asum += (1 << i - 1) * (i + one * 2)
        else:
            Asum += one
Bsum = 0
one = 0
for i in range(Blen):
    if B[i] == '1':
        one += 1
for i in range(Blen):
    if B[i] == '1':
        Bsum += 1
        one -= 1
        if i != 0:
            Bsum += (1 << i - 1) * (i + one * 2)
        else:
            Bsum += one
print(Bsum - Asum)
