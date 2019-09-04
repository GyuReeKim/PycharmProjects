# 두 개의 숫자열

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        maxV = -1000000
        for i in range(N-M+1):
            mul = 0
            for j in range(M):
                mul += A[i+j] * B[j]
            if mul > maxV:
                maxV = mul
        print('#{} {}'.format(tc, maxV))
    else:
        maxV = 0
        for i in range(M-N+1):
            mul = 0
            for j in range(N):
                mul += A[j] * B[i+j]
            if mul > maxV:
                maxV = mul
        print('#{} {}'.format(tc, maxV))
