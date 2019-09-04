# 숫자 카드

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input()))
    print(num)

    for i in range(N, 0, -1):
        for j in range(i-1):
            if num[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
    print(num)

    cnt = 1
    maxC = 0
    maxV = 0
    for i in range(1, N):
        if num[i] > num[i-1]:
            cnt = 1
            if cnt >= maxC:
                maxC = cnt
                maxV = num[i]
        elif num[i] == num[i-1]:
            cnt += 1
            if cnt >= maxC:
                maxC = cnt
                maxV = num[i]

    print('#{} {} {}'.format(tc, maxV, maxC))