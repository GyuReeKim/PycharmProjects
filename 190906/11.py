# [Professional] 쥬스 나누기

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    result = []
    for i in range(N):
        result.append('1/{}'.format(N))
    print('#{} {}'.format(tc, ' '.join(result)))