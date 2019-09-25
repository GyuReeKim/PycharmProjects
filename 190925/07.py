# [모의 SW 역량테스트] 수영장


def day(i):
    return schedule[i]*d


def month(i):
    if schedule[i] != 0:
        return m
    return 0


T = int(input())
for tc in range(1, T+1):
    d, m, m3, y = map(int, input().split())
    schedule = list(map(int, input().split()))
    print(d, m, m3, y)
    print(schedule)

    # 하루 이용권만 이용하는 경우
    only_day = 0
    for i in range(12):
        only_day += schedule[i]*d
    print(only_day)

    # 1달 이용권만 이용하는 경우
    only_month = 0
    for i in range(12):
        only_month += month(i)
    print(only_month)

    # 1년 이용권을 이용하는 경우
    only_year = y
    print(only_year)

    # 3달 이용권을 이용하는 경우
