#  8일차 - subtree


def order(n):
    global cnt
    if n > 0:
        cnt += 1
        # print(n, end=' ')
        order(ch1[n])
        order(ch2[n])


T = int(input())
for tc in range(1, T+1):
    E, N = list(map(int, input().split()))
    node = list(map(int, input().split()))

    ch1 = [0]*(E+2)
    ch2 = [0]*(E+2)
    par = [0]*(E+2)

    for i in range(E):
        p = node[2*i]
        c = node[2*i+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
        par[c] = p

    print(ch1)
    print(ch2)
    print(par)

    cnt = 0
    order(N)
    print('#{} {}'.format(tc, cnt))

