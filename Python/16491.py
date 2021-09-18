import itertools as T
I=input
R=range
def w(p,q):return p[0]*q[1]-p[1]*q[0]
def c(p,q,r):return w([q[0]-p[0],q[1]-p[1]],[r[0]-q[0],r[1]-q[1]])
def t(p,q,r,s):
    a=c(p,q,r)*c(p,q,s);b=c(r,s,p)*c(r,s,q)
    if a==b==0:return min(p,q)<=max(r,s)and min(r,s)<=max(p,q)
    return a<=0and b<=0
def d(x):
    for i in K:
        for j in R(i+1,N):
            if t(B[i],V[x[i]],B[j],V[x[j]]):return
    for i in x:print(i+1)
    exit()
N=int(I())
K=R(N)
C=T.permutations(K)
B=[list(map(int, I().split())) for _ in K]
V=[list(map(int, I().split())) for _ in K]
for i in C:d(i)