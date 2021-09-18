import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().split()))
    one = num.index(1)
    left = 0
    leftcancel = 0
    for i in range(one - 1, -1, -1):
        if num[i] > num[i + 1]:
            left += 1
        else:
            if left == 1:
                for j in range(i, -1, -1):
                    if num[j] < num[j + 1]:
                        leftcancel += 1
                    else:
                        break
            break
    right = 0
    rightcancel = 0
    for i in range(one + 1, N):
        if num[i] > num[i - 1]:
            right += 1
        else:
            if right == 1:
                for j in range(i, N):
                    if num[j] < num[j - 1]:
                        rightcancel += 1
                    else:
                        break
            break
    remain = N - left - right - leftcancel - rightcancel - 1
    # print(left, right, leftcancel, rightcancel, remain)
    if len(num) == 1:
        # print(1)
        print('Alice')
    elif left != 0 and right != 0:
        # print(2)
        if left > right and (remain + left + right + rightcancel) % 2:
            print('Bob')
        elif left < right and (remain + left + right + leftcancel) % 2:
            print('Bob')
        elif not (remain + left + right + rightcancel) % 2 or not (remain + left + right + leftcancel) % 2:
            print('Alice')
        else:
            print('Bob')
    else:
        # print(3)
        if not (remain + left + right) % 2:
            print('Alice')
        else:
            print('Bob')
