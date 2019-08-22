# 두 개의 숫자열

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N < M:
        maxV = 0
        for k in range(M-N+1):
            result = 0
            # maxV = 0
            for i in range(N):
                for j in range(M):
                    if j == i + k:
                        result += A[i] * B[j]
            # print(result)
            if result > maxV:
                maxV = result

        print('#{} {}'.format(tc, maxV))

    else:
        maxV = 0
        for k in range(N-M+1):
            result = 0
            # maxV = 0
            for i in range(N):
                for j in range(M):
                    if i == j + k:
                        result += A[i] * B[j]
            # print(result)
            if result > maxV:
                maxV = result

        print('#{} {}'.format(tc, maxV))
