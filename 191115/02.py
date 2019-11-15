# [모의 SW 역량테스트] 디저트 카페
# 시간초과 & 오답

import pprint
import sys
sys.stdin = open('test.txt', 'r')


def dfs(i, j, visited, s, d, n):
    global cnt
    d_count = 0
    for k in range(4):
        if d[k] == 0:
            d_count += 1
    # print(s, d_count)
    if d_count >= 3:
        if [i, j] in [[startI+1, startJ+1], [startI+1, startJ-1], [startI-1, startJ-1], [startI-1, startJ+1]]:
            if len(s) == len(set(s)):
                print(s)
                if len(s) > cnt:
                    cnt = len(s)
    if d_count >= 4:
        if [i, j] in [[startI+1, startJ+1], [startI+1, startJ-1], [startI-1, startJ-1], [startI-1, startJ+1]]:
            if len(s) == len(set(s)):
                print(s)
                if len(s) > cnt:
                    cnt = len(s)
    else:
        now_direction = -1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] != 0:
                    now_direction = k
                    if d[k] == 1:
                        d[k] = 0
                        dfs(ni, nj, visited, s + [visited[ni][nj]], d, now_direction)
                        d[k] = 1
                    else:
                        if n == now_direction:
                            dfs(ni, nj, visited, s + [visited[ni][nj]], d, n)


def bfs(i, j):
    global cnt
    dessert = []
    q = [''] * N * N
    visited = [[0] * N for _ in range(N)]
    start, end = -1, -1

    visited[i][j] = cafe[i][j]
    dessert.append(cafe[i][j])
    end += 1
    q[end] = [i, j]

    while start != end:
        start += 1
        si, sj = q[start][0], q[start][1]
        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                # 겹치는 디저트가 없다면
                if cafe[ni][nj] not in dessert:
                    visited[ni][nj] = cafe[ni][nj]
                    dessert.append(cafe[ni][nj])
                    end += 1
                    q[end] = [ni, nj]
    # print(i, j)
    # pprint.pprint(visited, indent=4, width=N*10)
    d = [1, 1, 1, 1]
    origin_direction = -1
    cnt = -1
    dfs(startI, startJ, visited, [visited[startI][startJ]], d, origin_direction)


# 방향을 총 3번 바꿀 수 있다.
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    # print(cafe)
    exclude = [[0, 0], [0, N - 1], [N - 1, 0], [N - 1, N - 1]]

    maxV = -1
    for i in range(N):
        for j in range(N):
            if [i, j] not in exclude:
                startI, startJ = i, j
                bfs(startI, startJ)
                if cnt > maxV:
                    maxV = cnt
    print('#{} {}'.format(tc, maxV))