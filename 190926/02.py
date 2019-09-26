# 0/1 Knapsack


def f(i, N, K, V, C):
    global maxV
    global cnt
    cnt += 1
    print(V, C)
    if V > K: # 가방 부피보다 물건 부피가 클 경우
        print('return')
        return
    elif i == N:
        print(C)
        if C > maxV:
            maxV = C
    else:
        # f(i+1, N, K, V+info[i][0], C+[info[i][1]])
        f(i+1, N, K, V, C)
        f(i+1, N, K, V+info[i][0], C+info[i][1])


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    info.sort(key=lambda x:(x[0]), reverse=True)
    print(info)
    maxV = 0
    cnt = 0
    f(0, N, K, 0, 0)
    print('#{} {}'.format(tc, maxV))
    print(cnt)