# 보물왕 태혁

T = int(input())
for tc in range(1, T+1):
    P = int(input())
    num = list(map(int, input().split()))
    minV = 1000000
    maxV = 0
    for i in range(P):
        if num[i] < minV:
            minV = num[i]
        if num[i] > maxV:
            maxV = num[i]
    print('#{} {}'.format(tc, minV*maxV))