def hanoi(n, former, latter):
    if n <= 0:
        return
    aux = 6 - former - latter
    hanoi(n - 1, former, aux)
    print(former, latter)
    hanoi(n - 1, aux, latter)

N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 3)
