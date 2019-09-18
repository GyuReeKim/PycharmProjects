# 화물 도크

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N, 0, -1):
        for j in range(i-1):
            if time[j][1] > time[j+1][1]:
                time[j], time[j+1] = time[j+1], time[j]
    print(time)

    cnt = 0
    finish = 0
    for i in range(N):
        if time[i][0] >= finish:
            finish = time[i][1]
            cnt += 1
    print('#{} {}'.format(tc, cnt))