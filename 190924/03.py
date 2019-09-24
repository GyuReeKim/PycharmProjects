# 창용 마을 무리의 개수 (상호배타집합)
# 오류 (set이 문제)


def rep(n):
    while p[n] != n:
        n = p[n]
    return n


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    p = [_ for _ in range(N+1)]
    # print(p)
    num = [list(map(int, input().split())) for _ in range(M)]
    # print(num)
    num.sort(key=lambda x:x[0])
    # print(num)
    for i in range(M):
        if len(num[i]) == 2:
            n1, n2 = num[i][0], num[i][1]
            p[rep(n2)] = rep(n1)
            # print(p)
    print('#{} {}'.format(tc, len(set(p))-1))