# 삼성시의 버스 노선

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus_stop = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = [int(input()) for _ in range(P)]

    result = []
    for i in range(P):
        cnt = 0
        for j in range(N):
            if bus_stop[j][0] <= C[i] <= bus_stop[j][1]:
                cnt += 1
        result.append(str(cnt))
    print('#{} {}'.format(tc, ' '.join(result)))
