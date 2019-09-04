# 구간합

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    num = list(map(int, input().split()))

    maxV = 0
    minV = 1000000
    for i in range(N-M+1):
        add = 0
        for j in range(M):
            add += num[i+j]
        if add > maxV:
            maxV = add
        if add < minV:
            minV = add

    print('#{} {}'.format(tc, maxV - minV))