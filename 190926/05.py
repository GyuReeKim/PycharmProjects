# 2일차 - Sum 변형문제

import sys
sys.stdin=open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    t = int(input())
    N = 100
    cost = [list(map(int, input().split())) for _ in range(N)]
    # print(cost)
    idxI = 0
    idxJ = 0
    minV = 1000000
    idxK = 0
    for k in range(30):
        for i in range(N):
            for j in range(N):
                s = 0
                for l in range(N):
                    s += abs(cost[i][l] - (k+1))
                    s += abs(cost[l][j] - (k+1))
                s -= abs(cost[i][j] - (k+1))
                if s < minV:
                    minV = s
                    idxK = k
    print('#{} {} {}'.format(tc, minV, idxK))