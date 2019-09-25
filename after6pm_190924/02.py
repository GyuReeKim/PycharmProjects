# 백준 - 캐슬 디펜스


def defence(aw1, aw2, aw3, N, M, D):
    # bfs에 방향?
    shoot(aw1, target, N, M, D)
    shoot(aw2, target, N, M, D)
    shoot(aw3, target, N, M, D)


def shoot(aw, target, N, M, D):
    # dfs 구현


N, M, D = map(int, input().split())
enemy = [list(map(int, input())) for _ in range(N)]
maxV = 0
for i in range(1, M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            kill = defence(i, j, k, N, M, D)
            if maxV < kill:
                maxV = kill
print(maxV)