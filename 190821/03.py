# 파리잡기
T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    add_max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            add = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    if k == i or k == i+M-1:
                        add += arr[k][l]
                if k != i and k != i+M-1:
                    add += arr[k][j]
                    add += arr[k][j+M-1]
            # print(add)
            if add > add_max:
                add_max = add
    print('#{} {}'.format(tc, add_max))

    # 가운데 값만 뺀 리스트 만드는 코드
    # for i in range(N-M+1):
    #     for j in range(N-M+1):
    #         add = []
    #         for k in range(i, i+M):
    #             row = []
    #             for l in range(j, j+M):
    #                 if k == i or k == i+M-1:
    #                     row.append(arr[k][l])
    #             if k != i and k != i+M-1:
    #                 row.append(arr[k][j])
    #                 row.append(arr[k][j+M-1])
    #             add.append(row)
    #         print(add)


