# 백준 7576번 토마토
# 푸는중

import sys
sys.stdin=open('01.txt', 'r')


def bfs(q):
    global visited
    start = -1
    end = len(q)-1
    while start == end:
        pass


N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(M)]
print(box)

visited = [[0 for j in range(N)] for i in range(M)]
print(visited)

q = []
for i in range(M):
    for j in range(N):
        if box[i][j] == 1:
            q.append([i, j])

print(bfs(q))
