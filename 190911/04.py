# 수의 새로운 연산
# import pprint


def point(k):
    for i in range(400):
        for j in range(400):
            if arr[i][j] == k:
                y = i
                x = j
                # print([x, y])
                return [x, y]

arr = [[1]]
for i in range(1, 400):
    arr.append([arr[i-1][0]+i])

for i in range(400):
    for j in range(1, 400):
        arr[i].append(arr[i][-1]+i+j+1)

# pprint.pprint(arr, indent=4, width=2000)

T = int(input())
for tc in range(1, T+1):
    p, q = list(map(int, input().split()))

    first = point(p)
    # print(first)
    second = point(q)
    # print(second)

    for i in range(400):
        for j in range(400):
            if i == first[-1] + second[-1] and j == first[0] + second[0]:
                print('#{} {}'.format(tc, arr[i+1][j+1]))