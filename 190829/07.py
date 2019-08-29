# 항구에 들어오는 배


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

    count = 0
    period_list = []
    for i in range(1, N):
        period = ship[i] - ship[0]
        if len(period_list) == 0 or double(period_list, period) == 1:
            period_list.append(period)
            count += 1

    print('#{} {}'.format(tc, count))