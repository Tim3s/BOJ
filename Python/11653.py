index = 2
N = int(input())
if N != 1:
    while index < N:
        if N % index == 0:
            print(index)
            N /= index
        else:
            index += 1
    print(index)
