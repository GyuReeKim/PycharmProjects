# 거듭 제곱


def square(N):
    global n
    result = N * n
    return result

T = 10
for tc in range(1, T+1):
    t = int(input())
    N, M = list(map(int, input().split()))
    n = N

    for i in range(M-1):
        N = square(N)
    print('#{} {}'.format(tc, N))