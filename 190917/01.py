# 백만장자 프로젝트

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    maxP = num[-1]
    sold = 0
    for i in range(N-2, -1, -1):
        if num[i] > maxP:
            maxP = num[i]
        else:
            sold += (maxP - num[i])
    print('#{} {}'.format(tc, sold))