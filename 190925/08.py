# 2차원 배열 4분할 문제


def f(a, b, c, d):
    s = 0
    for i in range(c-a+1):
        for j in range(d-b+1):
            s += arr[i+a][j+b]
    return s


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N-1):
    for j in range(N-1):
        print(f(0, 0, i, j))
        print(f(0, j+1, i, N-1))
        print(f(i+1, 0, N-1, j))
        print(f(i+1, j+1, N-1, N-1))
        print()