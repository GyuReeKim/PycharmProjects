# 항구에 들어오는 배
# 오류


def double(period_list, period):
    for p in period_list:
        if period % p == 0:
            return 0
    return 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ship = [int(input()) for _ in range(N)]
    # print(ship)

    idx = 1
    count = 0
    period_list = []
    for i in range(1, N):
        if i == idx:
            # print(idx)
            count += 1
            period = ship[idx] - ship[0]
            if len(period_list) == 0 or double(period_list, period) == 1:
                print(period-1)
                for j in range(2, N):
                    if ship[j] - ship[idx] != period:
                        idx = j
                        break
                        # print(idx)
    print('#{} {}'.format(tc, count))