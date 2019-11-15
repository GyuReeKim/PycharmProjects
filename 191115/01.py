# [모의 SW 역량테스트] 디저트 카페
# 잘못풀었음

import pprint
import sys
sys.stdin = open('test.txt', 'r')


def is_end_square(side, end, side_d, visited):
    global add
    for s in range(2):
        sideI, sideJ = side[s][0] - end[0], side[s][1] - end[1]
        is_possible = 0
        for k in range(4):
            for n in range(1, N):
                if sideI == n * di[k] and sideJ == n * dj[k]:
                    is_possible = 1
                    break
            if is_possible == 1:
                side_d[k] += 1
                break
    if len(set(side_d)) == 1:
        add = visited[startI][startJ] + visited[side[0][0]][side[0][1]] + visited[side[1][0]][side[1][1]] + visited[end[0]][end[1]]
        # print(add)


def is_square(side, end, visited):
    # print(side)
    side_d = [0, 0, 0, 0]
    for s in range(2):
        # 중심좌표와 side좌표의 거리 비율 차이로 직각인지 판단
        sideI, sideJ = side[s][0] - startI, side[s][1] - startJ
        is_possible = 0
        for k in range(4):
            for n in range(1, N):
                if sideI == n*di[k] and sideJ == n*dj[k]:
                    is_possible = 1
                    break
            if is_possible == 1:
                side_d[k] += 1
                break
    # print(side_d)
    line = [[0, 2], [1, 3]]
    not_square = 0
    one_count = 0
    is_line = 0
    side_line = []
    for k in range(4):
        if side_d[k] == 1:
            one_count += 1
            side_line += [k]
        if one_count > 2:
            not_square = 1
            break
        if side_line in line:
            is_line = 1
            break
    if one_count < 2:
        not_square = 1
    if is_line == 0 and not_square == 0:
        is_end_square(side, end, side_d, visited)


def side_end(i, j, visited):
    global point
    exist = []
    for r in range(N):
        for c in range(N):
            if visited[r][c] != 0 and [r, c] != [i, j]:
                exist += [[r, c]]
    # print(exist)
    for r in range(1, 1<<len(exist)):
        point = []
        for c in range(len(exist)):
            if r & (1<<c):
                point += [exist[c]]
        if len(point) == 3:
            for k in range(1, 1<<3):
                side = []
                end = []
                for l in range(3):
                    if k & (1<<l):
                        side += [point[l]]
                    else:
                        end += point[l]
                if len(side) == 2:
                    is_square(side, end, visited)


def bfs(i, j):
    global add
    dessert = []
    q = ['']*N*N
    visited = [[0]*N for _ in range(N)]
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
            if 0 <= ni < N and 0<= nj < N and visited[ni][nj] == 0:
                # 겹치는 디저트가 없다면
                if cafe[ni][nj] not in dessert:
                    visited[ni][nj] = cafe[ni][nj]
                    end += 1
                    q[end] = [ni, nj]
    # print(i, j)
    # pprint.pprint(visited, indent=4, width=N*10)
    side_end(i, j, visited)
    print(add)



# 방향을 총 3번 바꿀 수 있다.
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]
d = [[1, 1], [1, -1], [-1, -1], [-1, 1]]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    # print(cafe)
    exclude = [[0, 0], [0, N-1], [N-1, 0], [N-1, N-1]]

    maxV = 0
    for i in range(N):
        for j in range(N):
            if [i, j] not in exclude:
                startI, startJ = i, j
                bfs(startI, startJ)
                print()