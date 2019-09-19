# 전자카트


def f(n, k):
    global minV
    if n == k:
        c = 0
        new = [0]+p+[0]
        # print(new)
        for i in range(len(new)-1):
            c += golf[new[i]][new[i+1]]
        if c < minV:
            minV = c
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            f(n+1, k)
            p[n], p[i] = p[i], p[n]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    golf = [list(map(int, input().split())) for _ in range(N)]
    # print(golf)
    p = [_ for _ in range(1, N)]
    minV = 1000000
    f(0, N-1)
    print('#{} {}'.format(tc, minV))