# 백준 2178번 미로 탐색


def bfs(i, j):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    start = -1
    end = -1
    q = ['' for _ in range(N*M)]

    visited = [[0 for j in range(M)] for i in range(N)]

    end += 1
    q[end] = [i, j]
    visited[q[end][0]][q[end][1]] = 1
    # print(q)
    # print(visited)

    while start != end:
        start += 1
        i = q[start][0]
        j = q[start][1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < N and nj >= 0 and nj < M and visited[ni][nj] == 0:
                if maze[ni][nj] == '1':
                    visited[ni][nj] = visited[i][j] + 1
                    # print(visited)
                    end += 1
                    q[end] = [ni, nj]
    # print(visited)
    return visited[N-1][M-1]


N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
# print(maze)
print(bfs(0, 0))