# 최적 경로


def perm(n, k):
    global minV
    if n == k:
        # print(p)
        d = 0
        for i in range(N+1):
            if i == 0:
                d += (abs(company[0]-customer[2*p[i]]) + abs(company[1]-customer[2*p[i]+1]))
            elif i == N:
                d += (abs(customer[2*(p[i-1])]-home[0]) + abs(customer[2*(p[i-1])+1]-home[1]))
            else:
                d += (abs(customer[2*(p[i-1])]-customer[2*p[i]]) + abs(customer[2*(p[i-1])+1]-customer[2*p[i]+1]))
        # print(d)
        if d < minV:
            minV = d
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            perm(n+1, k)
            p[n], p[i] = p[i], p[n]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    point = list(map(int, input().split()))
    # print(point)
    company = point[:2]
    home = point[2:4]
    customer = point[4:]
    p = [_ for _ in range(N)]
    minV = 1000000
    perm(0, N)
    print('#{} {}'.format(tc, minV))