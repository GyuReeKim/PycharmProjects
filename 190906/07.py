# 장훈이의 높은 선반

T = int(input())
for tc in range(1, T+1):
    N, B = list(map(int, input().split()))
    H = list(map(int, input().split()))

    tower = []
    for i in range(1<<N):
        height = []
        for j in range(N):
            if i & (1<<j) != 0:
                height.append(H[j])
        tower.append(sum(height))
    # print(tower)

    min_tower = []
    for t in range(len(tower)):
        if tower[t] >= B:
            min_tower.append(tower[t] - B)
    print('#{} {}'.format(tc, min(min_tower)))