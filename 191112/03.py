# [모의 SW 역량테스트] 점심 식사시간
# 푸는중

import sys
sys.stdin=open('input.txt', 'r')

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def bfs(i, j):
    global visited, one, two
    q = ['']*N*N
    visited = [[0 for b in range(N)] for a in range(N)]
    start = -1
    end = -1

    visited[i][j] = 1
    end += 1
    q[end] = [i, j]

    one = ''
    two = ''
    while start != end:
        start += 1
        i = q[start][0]
        j = q[start][1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < N and nj >= 0 and nj < N and visited[ni][nj] == 0:
                visited[ni][nj] = visited[i][j] + 1
                if stairs_1 == [ni, nj]:
                    one = [visited[ni][nj], 1]
                if stairs_2 == [ni, nj]:
                    two = [visited[ni][nj], 2]
                if one == 1 and two == 1:
                    return
                end += 1
                q[end] = [ni, nj]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lunch = [list(map(int, input().split())) for _ in range(N)]
    print(lunch)

    stairs = []
    for i in range(N):
        for j in range(N):
            if lunch[i][j] != 0 and lunch[i][j] != 1:
                stairs.append([i, j])
    print(stairs)
    stairs_1 = stairs[0]
    stairs_2 = stairs[1]

    for i in range(N):
        for j in range(N):
            if lunch[i][j] == 1:
                bfs(i, j)
                print(one, two)
