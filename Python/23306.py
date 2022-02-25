import sys

N = int(sys.stdin.readline())
print("? 1")
sys.stdout.flush()
one = int(sys.stdin.readline())
print("?", N)
sys.stdout.flush()
last = int(sys.stdin.readline())
print("!", 1 if last > one else (0 if last == one else -1))
sys.stdout.flush()
