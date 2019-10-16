# 화섭이의 정수 나열
# 시간초과

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = []
    while len(num) != N:
        num += list(input().split())
    # print(num)
    cnt = 0
    while True:
        check = 0
        for i in range(N):
            add = ''
            for j in range(i, N):
                add += num[j]
                if add == str(cnt):
                    check = 1
        if check == 0:
            break
        cnt += 1
    print('#{} {}'.format(tc, cnt))