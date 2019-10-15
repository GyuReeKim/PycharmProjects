# 항구에 들어오는 배

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    happy = [int(input()) for _ in range(N)]
    # print(happy)

    cnt = 0
    period = 0
    while len(happy) != 0:
        ship = []
        cnt += 1
        for i in range(1, len(happy)):
            if i == 1:
                if (happy[i]-1) != period:
                    period = happy[i]-1
            if (happy[i]-1) % period != 0:
                ship.append(happy[i])
        if len(ship) != 0:
            happy = [1] + ship
        else:
            happy = ship
    print('#{} {}'.format(tc, cnt))