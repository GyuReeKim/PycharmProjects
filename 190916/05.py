# 달팽이 숫자

T = int(input())
for tc in range(1, T+1):
    cnt = 1
    N = int(input())
    k = N
    dir = 1
    arr = [[0]*N for _ in range(N)]

    i = 0
    j = -1

    while(1):
        for h in range(k):
            j += dir
            arr[i][j] = cnt
            cnt += 1
        k -= 1
        if k == 0:
            break
        for v in range(k):
            i += dir
            arr[i][j] = cnt
            cnt += 1
        dir *= -1

    print('#{}'.format(tc))
    result = [arr[i][j] for i in range(N) for j in range(N)]
    for i in range(len(result)):
        if i != 0 and i % N == 0:
            print()
        print(result[i], end=' ')
    print()

    # for i in range(N):
    #     for j in range(N):
    #         arr[i][j] = str(arr[i][j])

    # print('#{}'.format(tc))
    # for i in range(N):
    #     print(' '.join(arr[i]))