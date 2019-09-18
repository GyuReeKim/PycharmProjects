# 베이비진 게임
# 탐욕으로 풀기


def check(p):
    idx = [0]*10
    for i in range(len(p)):
        idx[p[i]] += 1
        if idx[p[i]] >= 3:
            return 1
    for k in range(8):
        if idx[k] != 0 and idx[k+1] != 0 and idx[k+2] != 0:
            return 1


T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    p1 = []
    p2 = []
    result = 0
    for i in range(12):
        if i % 2 == 0:
            p1.append(card[i])
        else:
            p2.append(card[i])
        if i >= 4:
            if i % 2 == 0:
                if check(p1) == 1:
                    result = 1
                    break
            else:
                check(p2)
                if check(p2) == 1:
                    result = 2
                    break
    print('#{} {}'.format(tc, result))