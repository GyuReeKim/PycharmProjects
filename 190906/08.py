# 장훈이의 높은 선반


def tower(N, B):
    global H
    minV = 1000000
    for i in range(1, 1<<N):
        height = 0
        for j in range(N):
            if i & (1<<j) != 0:
                height += H[j]
        if height >= B:
            if height < minV:
                minV = height
    return minV


T = int(input())
for tc in range(1, T+1):
    N, B = list(map(int, input().split()))
    H = list(map(int, input().split()))
    minV = tower(N, B)
    print('#{} {}'.format(tc, minV-B))