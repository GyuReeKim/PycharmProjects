# 파핑파핑 지뢰찾기

import sys
sys.stdin = open('04.txt', 'r')


def count(i, j):
    cnt = 0
    for k in range(8):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if game[ni][nj] == '*':
                cnt += 1
    return cnt


def bfs(i, j):
    global q, visited, start, end

    game[i][j] = 0
    visited[i][j] = 1
    end += 1
    q[end] = [i, j]

    while start != end:
        start += 1
        i, j = q[start][0], q[start][1]

        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if count(ni, nj) == 0:
                    game[ni][nj] = 0
                    visited[ni][nj] = 1
                    end += 1
                    q[end] = [ni, nj]
                else:
                    game[ni][nj] = count(ni, nj)
                    visited[ni][nj] = 1


di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    game = [list(input()) for _ in range(N)]
    # print(game)
    q = ['']*N*N
    visited = [[0 for b in range(N)] for a in range(N)]
    start = -1
    end = -1

    press = 0
    for i in range(N):
        for j in range(N):
            if game[i][j] == '.' and count(i, j) == 0:
                press += 1
                bfs(i, j)
                # print(press, [i, j])
    # print(game)
    for i in range(N):
        for j in range(N):
            if game[i][j] == '.':
                press += 1
    print('#{} {}'.format(tc, press))