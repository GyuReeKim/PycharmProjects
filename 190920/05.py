# 부분집합의 합
# 재귀


def f(n, k):
    if k == 0:
        print(temp)
    elif n < k:
        return
    else:
        temp[k-1] = A[n-1]
        f(n-1, k-1)
        f(n-1, k)


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    temp = [0]*N
    cnt = 0
    f(12, N)
    print('#{} {}'.format(tc, cnt))