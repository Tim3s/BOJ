tile = [[0] * 5 for _ in range(25)]
tile[0] = [1, 0, 0, 0, 0]
tile[1] = [1, 1, 0, 1, 1]
for i in range(2, 22):
    tile[i][0] = tile[i - 1][0] + tile[i - 1][1] + tile[i - 1][3] + tile[i - 1][4] + tile[i - 2][0]
    tile[i][1] = tile[i - 1][0] + tile[i - 1][4]
    tile[i][2] = tile[i - 1][3]
    tile[i][3] = tile[i - 1][0] + tile[i - 1][2]
    tile[i][4] = tile[i - 1][0] + tile[i - 1][1]
for i in range(int(input())):
    print(tile[int(input())][0])
