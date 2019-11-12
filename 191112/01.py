# [모의 SW 역량테스트] 등산로 조성

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def dfs(i, j):
    global maxV
    if visited[i][j] > maxV:
        maxV = visited[i][j]

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if ni >= 0 and ni < N and nj >= 0 and nj < N and visited[ni][nj] == 0:
            if hiking[ni][nj] < hiking[i][j]:
                visited[ni][nj] = visited[i][j] + 1
                dfs(ni, nj)
    # visited를 초기화 해줘야 한다.
    visited[i][j] = 0


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    hiking = [list(map(int, input().split())) for _ in range(N)]
    # print(hiking)
    maxH = 0
    for i in range(N):
        for j in range(N):
            if hiking[i][j] > maxH:
                maxH = hiking[i][j]
    # print(maxH)

    maxV = 0
    for i in range(N):
        for j in range(N):
            # 등산로의 원래 높이 저장한다.
            origin = hiking[i][j]
            # k만큼 hiking[i][j]를 깎는다.
            for k in range(1, K+1):
                hiking[i][j] = origin - k
                # print(hiking)

                for r in range(N):
                    for c in range(N):
                        if hiking[r][c] == maxH:
                            visited = [[0 for b in range(N)] for a in range(N)]
                            visited[r][c] = 1
                            dfs(r, c)
            hiking[i][j] = origin
    print('#{} {}'.format(tc, maxV))