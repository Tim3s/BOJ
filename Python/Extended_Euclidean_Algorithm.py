# ax + by = c ( = gcd(a, b))
def gcd(a, b):
    if b == 0:
        return a, (1, 0)
    res = gcd(b, a % b)
    g = res[0]
    x, y = res[1]
    return g, (y, x - (a // b) * y)
