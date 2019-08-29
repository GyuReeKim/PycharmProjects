# 항구에 들어오는 배
# 오류

# 주기에 포함된 배를 지우고, 주기에 포함되지 않은 배의 목록을 만드는 함수
def ship(happy):
    new_happy = []
    if len(happy) == 1:
        return new_happy
    h_idx = 1
    period = happy[1] - happy[0]
    # print(period)
    for i in range(2, len(happy)):
        if happy[i] - happy[h_idx] != period:
            new_happy.append(happy[i])
        else:
            h_idx = i
    # print(new_happy)
    return new_happy

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    happy = [int(input()) for _ in range(N)]
    print(happy)

    cnt = 0
    while len(happy) != 0:
        cnt += 1
        happy = ship(happy)
        # print(happy)
    print('#{} {}'.format(tc, cnt))

    # 함수로 만들자
    # new_happy = []
    # h_idx = 1
    # period = happy[1] - happy[0]
    # print(period)
    # for i in range(2, len(happy)):
    #     if happy[i] - happy[h_idx] != period:
    #         new_happy.append(happy[i])
    #     else:
    #         h_idx = i
    # print(new_happy)

