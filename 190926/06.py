# ㄱ자 T자 등 구하기

# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr = [list(map(int, input().split())) for _ in range(3)]
for i in range(3):
    for j in range(3):
        s = 0
        for k in range(3):
            s += arr[i][k]
            s += arr[k][j]
        s -= arr[i][j]
        print(s)