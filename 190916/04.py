# 이진수2

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    cnt = 0
    result = ''
    while cnt < 13:
        N *= 2
        result += str(int(N))
        N -= int(N)
        cnt += 1
        if N == 0.0:
            break
        elif cnt == 13:
            result = 'overflow'
            break
    print('#{} {}'.format(tc, result))