# 조교의 성적 매기기

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    score = []
    for n in range(N):
        M, F, R = list(map(int, input().split()))
        All = 0.35 * M + 0.45 * F + 0.2 * R
        score.append(All)
    # print(score)
    scoreK = score[K-1]

    sort_score = score
    for s in range(N - 1, 0, -1):
        for i in range(s):
            if sort_score[i] < sort_score[i + 1]:
                temp = sort_score[i]
                sort_score[i] = sort_score[i + 1]
                sort_score[i + 1] = temp
    # print(sort_score)

    for g in range(len(grade)):
        for i in range(N):
            if sort_score[i] == scoreK:
                if g * N/10 < i+1 <=(g+1) * N/10:
                    print('#{} {}'.format(tc, grade[g]))
                    break
