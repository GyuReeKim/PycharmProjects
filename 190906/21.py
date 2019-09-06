# 준홍이의 카드놀이

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))

    add = []
    for i in range(1, N+1):
        for j in range(1, M+1):
            add.append(i+j)
    # print(add)

    cnt = 0
    result = [0]*40
    for i in range(len(add)):
        for k in range(40):
            if add[i] == k:
                result[k] += 1
    # print(result)
    max_result = max(result)

    idx = []
    for i in range(40):
        if result[i] == max_result:
            idx.append(str(i))
    print('#{} {}'.format(tc, ' '.join(idx)))