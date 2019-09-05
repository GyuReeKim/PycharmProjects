# 장애물 경주 난이도

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    obstacle = list(map(int, input().split()))

    upV = 0
    downV = 0
    for i in range(N-1):
        diff = obstacle[i+1] - obstacle[i]
        if diff >= 0:
            if diff > upV:
                upV = diff
        else:
            if abs(diff) > downV:
                downV = abs(diff)
    print('#{} {} {}'.format(tc, upV, downV))
