# 지그재그 숫자

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    result = 0
    for n in range(1, N+1):
        if n % 2:
            result += n
        else:
            result -= n
    print('#{} {}'.format(tc, result))