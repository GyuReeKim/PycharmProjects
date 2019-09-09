# 세가지 합 구하기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    if N % 2:
        s1 = (N+2)*(N//2) + 1
    else:
        s1 = (N+1)*(N//2)
    s2 = N * N
    s3 = N * N + N
    print('#{} {} {} {}'.format(tc, s1, s2, s3))

# s1 = N * (N+1) // 2