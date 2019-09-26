# [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용 변형문제

# import sys
# sys.stdin=open('input.txt', 'r')


def perm(n, k):
    global minV
    if n == k:
        s = 0
        for i in range(N):
            # print(local[i], fac[p[i]])
            s += abs(local[i][0] - fac[p[i]][0]) + abs(local[i][1] - fac[p[i]][1])
        # print(s)
        if s < minV:
            minV = s
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            perm(n+1, k)
            p[n], p[i] = p[i], p[n]


T = 1
for tc in range(1, T+1):
    N = int(input())
    p = [_ for _ in range(N)]
    local = [list(map(int, input().split())) for _ in range(N)]
    fac = [list(map(int, input().split())) for _ in range(N)]
    minV = 1000000
    perm(0, N)
    print('#{} {}'.format(tc, minV))