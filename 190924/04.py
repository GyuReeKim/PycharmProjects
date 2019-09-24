# 창용 마을 무리의 개수 (상호배타집합)


def rep(n):
    while p[n] != n:
        n = p[n]
    return n


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    p = [_ for _ in range(N+1)]
    num = [list(map(int, input().split())) for _ in range(M)]
    # num.sort(key=lambda x:(x[0], x[1]))
    # print(num)
    for i in range(M):
        p[rep(num[i][1])] = rep(num[i][0])
        # print(p)
    cnt = 0
    for i in range(1, N+1):
        if p[i] == i:
            cnt += 1
    print('#{} {}'.format(tc, cnt))