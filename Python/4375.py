while True:
    try:
        N = int(input())
    except:
        break
    i = 1
    rem = i % N
    while rem != 0:
        i += 1
        rem = (rem * 10 + 1) % N
    print(i)
