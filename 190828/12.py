T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))

    result = []
    for i in range(N-M+1):
        add = 0
        for j in range(i, i+M):
            add += A[j]
        result.append(add)
    print(result)

    maxV = 0
    minV = 1000000
    for i in range(len(result)):
        if result[i] > maxV:
            maxV = result[i]
        if result[i] < minV:
            minV = result[i]
    print('#{} {}'.format(tc, maxV-minV))

