# 당근밭 옆 고구마밭

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = list(map(int, input().split()))
    print(farm)

    maxV = 0
    temp = 0
    len = 0
    for i in range(1, N):
        if i == N-1:
