# [알고리즘 월말평가 문제3] : 미네랄 모으기
# 풀이중

import sys
sys.stdin = open('input.txt', 'r')


def perm(n, k):
    if n == k:
        for idx in range(len(mineral)):
            bfs(p[idx])
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            perm(n+1, k)
            p[n], p[i] = p[i], p[n]


def bfs(num):
    global energy
    q = ['']*N*M
    visited = [[0 for b in range(M)] for a in range(N)]
    start = -1
    end = -1

    visited[robot[0]][robot[1]] = 1
    end += 1
    q[end] = [robot[0], robot[1]]

    energy = 0
    distance = 0
    while start != end:
        start += 1
        i = q[start][0]
        j = q[start][1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < N and nj >= 0 and nj < M and visited[ni][nj] == 0:
                if ni == mineral[num][0] and nj == mineral[num][1]:
                    energy += mineral[num][2]
                    visited[ni][nj] = visited[i][j] + 1
                    end += 1
                    q[end] = [ni, nj]


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]
    print(box)

    mineral = []
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                robot = [i, j]
            elif box[i][j] != 0:
                mineral.append([i, j, box[i][j]])
    print(mineral)
    p = [_ for _ in range(len(mineral))]
    perm(0, len(mineral))
    print(energy)

