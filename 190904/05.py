# 중간 평균값 구하기

T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input().split()))

    for i in range(len(num), 0, -1):
        for j in range(i-1):
            if num[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp

    all = 0
    for i in range(len(num)):
        if i != 0 and i != len(num)-1:
            all += num[i]
    result = round(all/(len(num)-2))
    print('#{} {}'.format(tc, result))