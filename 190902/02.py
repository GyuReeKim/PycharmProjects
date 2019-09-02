# 수열 합치기

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))

    result = []
    for i in range(M):
        num_list = list(map(int, input().split()))
        # print(num_list)

        if len(result) == 0:
            result.extend(num_list)
            # print(result)

        else:
            for k in range(len(result)):
                if result[k] > num_list[0]:
                    left = result[:k]
                    right = result[k:]
                    break
            else:
                left = result
                right = []

            result = []
            result.extend(left)
            result.extend(num_list)
            result.extend(right)
            # print(result)

    # print(result)

    result = [str(result[i]) for i in range(len(result)-1, -1, -1) if i >= len(result) - 10]

    # for i in range(len(result)-1, -1, -1):
    #     if i >= len(result) - 10:
    #         print(result[i])

    #
    #
    # result = result[len(result)-10:]
    # result = [str(result[i]) for i in range(len(result)-1, -1, -1)]
    #
    print('#{} {}'.format(tc, ' '.join(result)))

