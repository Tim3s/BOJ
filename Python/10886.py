cute = 0
for i in range(int(input())):
    cute += float(input())-0.5
print("Junhee is not cute!" if cute < 0 else "Junhee is cute!")