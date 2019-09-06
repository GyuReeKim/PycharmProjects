# 장훈이의 높은 선반


def tower(N, B):
    global H
    minV = 0
    for i in range((1<<N)-1, 0, -1):
        height = 0
        for j in range(N):
            if i & (1<<j) != 0:
                height += H[j]
        if height >= B:
            minV = height
        else:
            return minV


T = int(input())
for tc in range(1, T+1):
    N, B = list(map(int, input().split()))
    H = list(map(int, input().split()))
    # H = sorted(H)
    minV = tower(N, B)
    # minV = 1000000
    # for i in range((1<<N)-1, 0, -1):
    #     height = 0
    #     for j in range(i):
    #         if i & (1<<j) != 0:
    #             height += H[j]
    #     print(height)
    #     if height >= B:
    #         if height < minV:
    #             minV = height
    print('#{} {}'.format(tc, minV-B))