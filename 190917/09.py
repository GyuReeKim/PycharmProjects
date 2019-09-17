# 2일차 - 최소합
# 윤선언니가 알려줌!!


def add(i, j, val):
    global minC
    if val > minC:
        return
    if i == N-1 and j == N-1:
        if val < minC:
            minC = val
    else:
        if j+1 < N:
            add(i, j+1, val + arr[i][j+1])
        if i+1 < N:
            add(i+1, j, val + arr[i+1][j])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    minC = 1000000
    res = [0]*(2*N-1)
    add(0, 0, arr[0][0])
    print('#{} {}'.format(tc, minC))