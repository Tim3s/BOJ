import sys

txt = sys.stdin.readline().rstrip()
N = len(txt)
while N:
    for i in range(N // 2):
        if txt[i] != txt[N - i - 1]:
            print('IPSELENTI')
            sys.exit(0)
    N //= 2
print('AKARAKA')
