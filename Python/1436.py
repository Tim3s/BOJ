N = int(input())
n = 666
counter = 0
while True:
    if '666' in str(n):
        counter += 1
    if counter == N:
        print(n)
        break
    n += 1
