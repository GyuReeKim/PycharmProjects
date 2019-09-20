# 부분집합의 합
# 재귀


def f(n, r):
    global cnt
    if r == 0:
        if sum(temp) == K:
            cnt += 1
    elif n < r:
        return
    else:
        temp[r-1] = A[n-1]
        f(n-1, r-1)
        f(n-1, r)


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    temp = [0]*N
    cnt = 0
    f(12, N)
    print('#{} {}'.format(tc, cnt))