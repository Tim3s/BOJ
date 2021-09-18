import sys
import copy

N = int(sys.stdin.readline())
newmat = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
mat = 0
while mat != newmat:
    mat = copy.deepcopy(newmat)
    for i in range(N):
        for j in range(N):
            if mat[i][j]:
                for k in range(N):
                    if newmat[k][i]:
                        newmat[k][j] = 1
                    if newmat[j][k]:
                        newmat[i][k] = 1
for i in range(N):
    print(' '.join([str(i) for i in mat[i]]))
