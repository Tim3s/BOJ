V=int(input())
A=input().count("A")
if A>V-A:
    print("A")
elif A*2==V:
    print("Tie")
else:
    print("B")
