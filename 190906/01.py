# 숫자를 정렬하자

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
    num = [str(num[i]) for i in range(N)]
    print('#{} {}'.format(tc, ' '.join(num)))