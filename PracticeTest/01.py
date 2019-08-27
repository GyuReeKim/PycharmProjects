T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = list(map(int, input().split()))
    maxV = -1000
    for i in range(N-1):
        for j in range(i+1, N):
            # print(P[j] - P[i])
            if P[j] - P[i] > maxV:
                maxV = P[j] - P[i]
    print('#{} {}'.format(tc, maxV))
