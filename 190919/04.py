# 최소 생산 비용


def f(n, k, c): # n:공장번호, k:공장 수 c:생산비용합
    global minV
    if n == k:
        # print(p)
        if c < minV:
            minV = c
            return
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            if minV < c:
                return
            f(n+1, k, c + V[p[n]][n])
            p[n], p[i] = p[i], p[n]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    # print(V)
    p = [_ for _ in range(N)]
    minV = 1000000
    f(0, N, 0)
    print('#{} {}'.format(tc, minV))