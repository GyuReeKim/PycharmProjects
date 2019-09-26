# [파이썬 S/W 문제해결 구현] 2일차 - 최소합


def f(i, j, s):
    global minV
    if s > minV:
        return
    elif i == N-1 and j == N-1:
        if s < minV:
            minV = s
    else:
        if i + 1 < N:
            f(i+1, j, s + arr[i+1][j])
        if j + 1 < N:
            f(i, j+1, s + arr[i][j+1])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 1000000
    f(0, 0, arr[0][0])
    print('#{} {}'.format(tc, minV))