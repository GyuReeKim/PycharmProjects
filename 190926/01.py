# 2일차 - Sum 변형문제

import sys
sys.stdin=open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    t = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    cost = [0]*30

    minV = 1000000
    idxI = 0
    for k in range(30):
        s1 = 0
        s2 = 0
        for i in range(N):
            s1 += abs(arr[i][i] - (k+1))
            s2 += abs(arr[i][30-(i+1)] - (k+1))
            r = 0
            c = 0
            for j in range(N):
                r += abs(arr[i][j] - (k+1))
                c += abs(arr[j][i] - (k+1))
            if r < minV:
                minV = r
                idxI = k+1
            if c < minV:
                minV = c
                idxI = k+1
        if s1 < minV:
            minV = s1
            idxI = k+1
        if s2 < minV:
            minV = s2
            idxI = k+1
    print('#{} {} {}'.format(tc, minV, idxI))