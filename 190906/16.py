# 동철이의 프로그래밍 대회

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))

    result = [0]*N
    score = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            result[i] += score[i][j]
    # print(result)

    cnt = 0
    max_score = 0
    for i in range(N):
        if result[i] >= max_score:
            max_score = result[i]
            cnt += 1
    print('#{} {} {}'.format(tc, cnt, max_score))