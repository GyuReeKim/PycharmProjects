# 두 개의 숫자열

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    maxV = -1000000
    if N > M:
        for i in range(N-M+1):
            add = 0
            for j in range(M):
                add += A[i+j]*B[j]
            if add > maxV:
                maxV = add
    else:
        for i in range(M-N+1):
            add = 0
            for j in range(N):
                add += A[j]*B[i+j]
            if add > maxV:
                maxV = add
    print('#{} {}'.format(tc, maxV))