# 새샘이의 7-3-5 게임

T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input().split()))

    add = []
    for i in range(1<<7):
        res = []
        for j in range(7):
            if i & (1<<j):
                res.append(num[j])
                if len(res) == 3:
                    add.append(sum(res))
                    break
    fifth = sorted(set(add))[-5]
    print('#{} {}'.format(tc, fifth))