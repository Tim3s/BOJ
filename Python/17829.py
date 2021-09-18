import sys


def pulling(mat, n):
    if n == 2:
        return sorted(mat[0] + mat[1])[2]
    res = []
    n //= 2
    res.append(pulling([cur[:n] for cur in mat[:n]], n))
    res.append(pulling([cur[n:] for cur in mat[:n]], n))
    res.append(pulling([cur[:n] for cur in mat[n:]], n))
    res.append(pulling([cur[n:] for cur in mat[n:]], n))
    return sorted(res)[2]


N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(pulling(matrix, N))
