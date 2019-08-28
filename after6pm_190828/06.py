# 상원이의 연속 합

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        s = 0
        for j in range(i, N+1):
            s += j
            if s == N:
                cnt += 1
                break
            elif s > N:
                break
    print('#{} {}'.format(tc, cnt))