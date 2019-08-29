# 항구에 들어오는 배
# 오류

def ship(N, happy, visit):
    for i in range(N):
        if visit[i] == 0:
            for j in range(i+1, N):
                period = happy[j] - happy[i]
                possible_cnt = (happy[-1] - happy[i]) // period
                cnt = 0
                for k in range(j+1, N):
                    if (happy[k] - happy[i]) % period == 0:
                        cnt += 1
                if cnt == possible_cnt:
                    for k in range(j, N):
                        if (happy[k] - happy[i]) % period == 0:
                            visit[i] = 1
                            visit[k] = 1
                else:
                    break
    return visit



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    happy = [int(input()) for _ in range(N)]
    print(happy)
    visit = [0 for _ in range(N)]
    print(visit)

    print(ship(N, happy, visit))


