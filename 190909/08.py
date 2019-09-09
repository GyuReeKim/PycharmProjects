# 수의 새로운 연산
# Runtime Error

import pprint


def point(k):
    for i in range(142):
        for j in range(i+1):
            if arr[i][j] == k:
                y = i
                x = j
                # print([x, y])
                return [x, y]


arr = [[0]*(142-_+1) for _ in range(142)]
num = 0
for i in range(142):
    for j in range(i):
        num += 1
        arr[j+1][i-j] = num
pprint.pprint(arr, indent=4, width=1420)

T = int(input())
for tc in range(1, T+1):
    p, q = list(map(int, input().split()))

    first = point(p)
    # print(first)
    second = point(q)
    # print(second)

    for i in range(142):
        for j in range(i+1):
            if i == first[-1] + second[-1] and j == first[0] + second[0]:
                print('#{} {}'.format(tc, arr[i][j]))

