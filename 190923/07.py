# 배열 최소 합


def perm(n, k, s):
    global minV
    if s > minV:
        return
    elif n == k:
        if s < minV:
            minV = s
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            perm(n+1, k, s + arr[n][p[n]])
            p[n], p[i] = p[i], p[n]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [_ for _ in range(N)]
    minV = 1000000
    perm(0, N, 0)
    print('#{} {}'.format(tc, minV))