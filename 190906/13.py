# 다양성 측정

T = int(input())
for tc in range(1, T+1):
    X = input()

    cnt = 0
    result = []
    for i in range(len(X)):
        if X[i] not in result:
            result.append(X[i])
            cnt += 1
    print('#{} {}'.format(tc, cnt))