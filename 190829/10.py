# 진기의 최고급 붕어빵

T = int(input())
for tc in range(1, T+1):
    N, M, K = list(map(int, input().split()))
    when = sorted([0]*K + list(map(int, input().split())))
    # print(when)

    result = 'Possible'
    for i in range(K, N+K):
        if i % K == 0:
            if when[i] - when[i-K] < M:
                result = 'Impossible'

    print('#{} {}'.format(tc, result))
