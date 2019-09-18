# 베이비진 게임


def perm(n, k, p):
    global judge
    if n == k:
        # print(p)
        if p[0] == p[1] == p[2]:
            judge = 1
        if p[2] == p[1]+1 == p[0]+2:
            judge = 1
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            perm(n+1, k, p)
            p[n], p[i] = p[i], p[n]


T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    # print(card)

    p1 = []
    p2 = []
    judge = 0
    result = 0
    for i in range(12):
        if i % 2 == 0:
            p1.append(card[i])
        else:
            p2.append(card[i])
        if i >= 4:
            if i % 2 == 0:
                perm(0, len(p1), p1)
                if judge == 1:
                    result = 1
                    break
            else:
                perm(0, len(p2), p2)
                if judge == 1:
                    result = 2
                    break
    print('#{} {}'.format(tc, result))