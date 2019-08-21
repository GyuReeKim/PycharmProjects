## 다시풀기
T = int(input())
for tc in range(T):
    print('#{}'.format(tc))
    N, K = list(map(int, input().split()))

    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    score = []
    for n in range(N):
        M, F, R = list(map(int, input().split()))
        All = M * 0.35 + F * 0.45 + R * 0.2
        score.append(All)
    print(score)

    sort_score = score
    for s in range(len(sort_score) - 1, 0, -1):
        for i in range(s):
            if sort_score[i] < sort_score[i + 1]:
                temp = sort_score[i]
                sort_score[i] = sort_score[i + 1]
                sort_score[i + 1] = temp
    print(sort_score)

    for ss in range(len(sort_score)):
        if sort_score[ss] == score[K-1]:
            print(ss+1)
