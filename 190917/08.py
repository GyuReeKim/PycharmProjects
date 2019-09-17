# 2일차 - 최소합
import pprint


def add(i, j, val):
    global minC
    di = [0, 1]
    dj = [1, 0]
    if val > minC:
        return
    if i == N-1 and j == N-1:
        if val < minC:
            minC = val
    else:
        for k in range(2):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < N and nj >= 0 and nj < N:
                add(ni, nj, val + arr[ni][nj])


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minC = 1000000
    add(0, 0, arr[0][0])
    print('#{} {}'.format(tc, minC))
    # pprint.pprint(arr, indent=4, width=N*10)