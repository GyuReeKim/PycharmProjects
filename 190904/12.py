# 부분집합의 합

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))

    cnt = 0
    for i in range(1<<12):
        res = []
        for j in range(12):
            if i & (1<<j) != 0:
                res.append(A[j])
        if len(res) == N and sum(res) == K:
            cnt += 1

    print('#{} {}'.format(tc, cnt))