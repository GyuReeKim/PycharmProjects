# 수열 합치기


def split(num_list, result):
    for i in range(len(result)):
        if result[i] > num_list[0]:
            left = result[:i]
            right = result[i:]
            break
    else:
        left = result
        right = []

    # result = left + num_list + right
    result = []
    result.extend(left)
    result.extend(num_list)
    result.extend(right)

    return result


T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))

    result = []
    for i in range(M):
        num_list = list(map(int, input().split()))

        result = split(num_list, result)

    result = [str(result[i]) for i in range(len(result)-1, -1, -1) if i >= len(result) - 10]

    print('#{} {}'.format(tc, ' '.join(result)))

