# 최장 증가 부분 수열


def f(n, k, t, l):
    global cnt
    cnt += 1
    if n == k:
        print(t, l)
    else:
        if len(t) == 0:
            f(n-1, k, t+[A[n-1]], l+1)
        elif len(t) != 0 and A[n-1] < t[-1]:
            f(n-1, k, t+[A[n-1]], l+1)
        f(n-1, k, t, l)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    temp = []
    cnt = 0
    f(N, 0, temp, 0)
    print(cnt)