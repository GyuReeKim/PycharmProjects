# 백준 7576번 토마토

import sys
sys.stdin=open('01.txt', 'r')


def bfs(i, j):
    global visited, q, start, end
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # print(visited)

    while start != end:
        start += 1
        i = q[start][0]
        j = q[start][1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < N and nj >= 0 and nj < M and visited[ni][nj] == 0:
                if box[ni][nj] == '0':
                    visited[ni][nj] = visited[i][j] + 1
                    end += 1
                    q[end] = [ni, nj]

    # print(visited)
    maxV = 0
    for r in range(N):
        for c in range(M):
            if visited[r][c] == 0:
                return -1
            elif visited[r][c] > maxV:
                maxV = visited[r][c]
    return maxV - 1


T = int(input())
for tc in range(1, T+1):
    M, N = map(int, input().split())
    box = [input().split() for _ in range(N)]
    # print(box)
    visited = [[0 for j in range(M)] for i in range(N)]
    # print(visited)
    q = ['']*N*M
    start = -1
    end = -1

    for i in range(N):
        for j in range(M):
            if box[i][j] == '1':
                visited[i][j] = 1
                end += 1
                q[end] = [i, j]
            if box[i][j] == '-1':
                visited[i][j] = -1

    # print(q)
    print(bfs(q[0][0], q[0][1]))