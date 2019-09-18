# 컨테이너 운반

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    for i in range(N, 0, -1): # 큰 컨테이너 순서로 정렬
        for j in range(i-1):
            if w[j] < w[j+1]:
                w[j], w[j+1] = w[j+1], w[j]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if t[j] >= w[i]:
                cnt += w[i]
                t[j] = -1
                break
    print('#{} {}'.format(tc, cnt))