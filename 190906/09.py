# 가능한 시험 점수
# 시간초과

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    point = list(map(int, input().split()))

    final = []
    for i in range(1<<N):
        score = 0
        for j in range(N):
            if i & (1<<j):
                score += point[j]
        # print(score)
        if score not in final:
            final.append(score)
    print('#{} {}'.format(tc, len(final)))