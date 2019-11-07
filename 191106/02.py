# 백준 7576번 토마토

import sys
sys.stdin=open('02.txt', 'r')


def bfs(i, j):
    global q, visited, start, end
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    while start != end:
        start += 1
        i = q[start][0]
        j = q[start][1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < M and nj >= 0 and nj < N and visited[ni][nj] == 0:
                if box[ni][nj] == '0':
                    visited[ni][nj] = visited[i][j] + 1
                    end += 1
                    q[end] = [ni, nj]
    print(visited)



N, M = map(int, input().split())
box = [input().split() for _ in range(M)]
# print(box)
visited = [[0 for j in range(N)] for i in range(M)]
# print(visited)

q = ['' for _ in range(N*M)]
start = -1
end = -1

for i in range(M):
    for j in range(N):
        if box[i][j] == '1':
            end += 1
            q[0] = [i, j]
            visited[i][j] = 1

print(bfs(q[0][0], q[0][1]))