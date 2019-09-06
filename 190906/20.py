# 보충학습과 평균

T = int(input())
for tc in range(1, T+1):
    score = list(map(int, input().split()))

    all = 0
    for i in range(5):
        if score[i] < 40:
            all += 40
        else:
            all += score[i]
    print('#{} {}'.format(tc, all//5))