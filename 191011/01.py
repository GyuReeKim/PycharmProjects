# 당근 수확 3

import sys
sys.stdin=open('input.txt', 'r')


def f(x, y, i, j):
    s = 0
    for r in range(i+1-x):
        for c in range(j+1-y):
            s += farm[x+r][y+c]
    return s


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    farm = [list(map(int, input().split())) for _ in range(N)]

    minV = 1000000
    # carrot = [0, 0, 0]
    for i in range(N-1):
        for j in range(M-1):
            s1 = f(0, 0, i, j)
            s2 = f(0, j+1, i, M-1)
            s3 = f(i+1, 0, N-1, M-1)
            diff = max(s1, s2, s3) - min(s1, s2, s3)
            # carrot[0] = s1
            # carrot[1] = s2
            # carrot[2] = s3
            # diff = max(carrot) - min(carrot)
            if diff < minV:
                minV = diff
    print('#{} {}'.format(tc, minV))