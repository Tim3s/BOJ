while(True):
    n = int(input())
    if n == -1: break
    factors = []
    for i in range(1, n//2+1):
        if n % i == 0:
            factors.append(i)
    if sum(factors) == n:
        print(f"{n} =", " + ".join(map(str, factors)))
    else:
        print(str(n), "is NOT perfect.")
