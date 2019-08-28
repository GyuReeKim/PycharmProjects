# min max

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    # # 버블정렬
    # for i in range(N-1, 0, -1):
    #     for j in range(i):
    #         if a[j] > a[j+1]:
    #             temp = a[j]
    #             a[j] = a[j+1]
    #             a[j+1] = temp
    # print(a)

    minV = a[0]
    maxV = a[0]
    for i in range(1, N):
        if a[i] < minV:
            minV = a[i]
        if a[i] > maxV:
            maxV = a[i]

    print('#{} {}'.format(tc, maxV - minV))