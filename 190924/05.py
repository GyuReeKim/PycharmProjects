# 상원이의 생일파티


def rep(n):
    while p[n] != n:
        n = p[n]
    return n


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    p = [_ for _ in range(N+1)]
    c = [0 for _ in range(N+1)]

    num = []
    for i in range(M):
        a, b = map(int, input().split())
        if a < b:
            num.append([a, b])
        else:
            num.append([b, a])
    num.sort(key=lambda x:x[0])
    # print(num)

    cnt = 0
    for i in range(M):
        if num[i][0] == 1:
            cnt += 1
            c[num[i][1]] = 1
            p[rep(num[i][1])] = p[rep(num[i][0])]
        elif c[num[i][0]] == 1:
            if p[num[i][1]] != 1:
                cnt += 1
            p[rep(num[i][1])] = p[rep(num[i][0])]
        elif c[num[i][1]] == 1:
            if p[num[i][0]] != 1:
                cnt += 1
            p[rep(num[i][0])] = p[rep(num[i][1])]
    print('#{} {}'.format(tc, cnt))