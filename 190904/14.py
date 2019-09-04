# 특별한 정렬

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    for i in range(N, 0, -1):
        for j in range(i-1):
            if num[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
    # print(num)

    result = []
    for i in range(10):
        if i % 2:
            result.append(str(num.pop(0)))
        else:
            result.append(str(num.pop()))
    print('#{} {}'.format(tc, ' '.join(result)))