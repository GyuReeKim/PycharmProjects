# 백준 16509번 장군
# 푸는중

import sys
sys.stdin=open('03.txt', 'r')


def bfs(i, j):
    di = [2, 3, 3, 2, -2, -3, -3, -2]
    dj = [3, 2, -2, -3, -3, -2, 2, 3]
    pi = [0, 1, 2, 1, 2, 1, 0, -1, -2, -1, -2, -1]
    pj = [1, 2, 1, 0, -1, -2, -1, -2, -1, 0, 1, 2]
    global visited, q, start, end

    visited[i][j] = 1
    end += 1
    q[end] = [i, j]
    # print(q)

    while start != end:
        start += 1
        i = q[start][0]
        j = q[start][1]
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            back = 0
            if ni >= 0 and ni < 9 and nj >= 0 and nj < 8 and visited[ni][nj] == 0:
                for p in range(12):
                    xi = i + pi[p]
                    xj = j + pj[p]
                    if king == [xi, xj]:
                        back = 1
                        break
                if back == 0:
                    pass




T = int(input())
for tc in range(1, T+1):
    user = list(map(int, input().split()))
    king = list(map(int, input().split()))

    visited = [[0 for j in range(8)] for i in range(9)]
    # print(visited)
    q = ['']*72
    start = -1
    end = -1

    bfs(user[0], user[1])