# 전기버스2


def f(n, m): # n:도착점, m:시작점
    global cnt
    # global cnt2
    # cnt2 += 1
    if m != 0:
        if m - n <= M[n]:
            cnt += 1
            f(0, n)
        else:
            f(n+1, m)


T = int(input())
for tc in range(1, T+1):
    NM = list(map(int, input().split()))
    N = NM[0]
    M = NM[1:]
    # print(N, M)
    cnt = 0
    # cnt2 = 0
    f(0, N-1)
    print('#{} {}'.format(tc, cnt-1))
    # print(cnt2)