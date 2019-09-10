# 태혁이의 사랑은 타이밍

T = int(input())
for tc in range(1, T+1):
    D, H, M = list(map(int, input().split()))

    day = D - 11
    hour = H - 11
    minute = M - 11

    if minute < 0:
        hour -= 1
        minute += 60

    if hour < 0:
        day -= 1
        hour += 24

    if day < 0:
        print('#{} -1'.format(tc))
    else:
        realize = day*24*60 + hour*60 + minute
        print('#{} {}'.format(tc, realize))