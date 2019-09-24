# 구간 자르기


def f(a, b, c, d):
    R = c - a + 1
    C = d - b + 1
    p = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            p[i][j] = arr[a+i][b+j]
    print(p)


N = 5
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

for i in range(N-1):
    for j in range(N-1):
        # if i == 1 and j == 1:
        f(0, 0, i, j)
        f(0, j+1, i, N-1)
        f(i+1, 0, N-1, j)
        f(i+1, j+1, N-1, N-1)