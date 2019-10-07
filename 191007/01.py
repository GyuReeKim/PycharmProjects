# 당근 수확

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = list(map(int, input().split()))

    idx = 0
    minV = 1000000
    for i in range(1, N):
        left = sum(farm[:i])
        right = sum(farm[i:])
        val = left-right
        if val < 0:
            val = -val
        if val < minV:
            idx = i
            minV = val
    print(f'#{tc} {idx} {minV}')