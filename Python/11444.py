import copy
def fibonacci(n):
    cur = [0, 1]
    nextone = [0, 0]
    res = [0, 1]
    while n > 0:
        if n % 2:
            nextone[0] = (cur[0] * res[0] + cur[1] * res[1]) % 1000000007
            nextone[1] = (cur[1] * res[0] + (cur[0] + cur[1]) * res[1]) % 1000000007
            res = copy.deepcopy(nextone)
        nextone[0] = (cur[0] ** 2 + cur[1] ** 2) % 1000000007
        nextone[1] = cur[1] * (2 * cur[0] + cur[1]) % 1000000007
        cur = copy.deepcopy(nextone)
        n //= 2
    return res[0]


n = int(input())
print(fibonacci(n))
