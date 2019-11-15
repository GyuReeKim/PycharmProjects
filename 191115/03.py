# [모의 SW 역량테스트] 특이한 자석

import pprint
import sys
sys.stdin = open('03.txt', 'r')


def rotate(magnet_number, rotation):
    global magnets
    q = ['']*4
    visited = [0 for _ in range(4)]
    start, end = -1, -1

    neighbors = [[magnets[0][2], magnets[1][6]], [[magnets[0][2], magnets[1][6]], [magnets[1][2], magnets[2][6]]], [[magnets[1][2], magnets[2][6]], [magnets[2][2], magnets[3][6]]], [magnets[2][2], magnets[3][6]]]
    # print(neighbors)
    r = [0, 0, 0, 0]

    r[magnet_number-1] = rotation
    visited[magnet_number-1] = 1
    end += 1
    q[end] = magnet_number-1

    while start != end:
        # print(q)
        # print(r)
        start += 1
        i = q[start]
        # print(i)
        for k in range(2):
            ni = i + di[k]
            if 0 <= ni < 4 and visited[ni] == 0:
                if i == 0 or i == 3:
                    # print(i, k, neighbors[i])
                    if neighbors[i][0] != neighbors[i][1]:
                        r[ni] = -r[i]
                        visited[ni] = visited[i] + 1
                        end += 1
                        q[end] = ni
                elif i == 1 or i == 2:
                    # print(i, k, neighbors[i][k])
                    if k == 0:
                        if neighbors[i][1][0] != neighbors[i][1][1]:
                            r[ni] = -r[i]
                            visited[ni] = visited[i] + 1
                            end += 1
                            q[end] = ni
                    elif k == 1:
                        if neighbors[i][0][0] != neighbors[i][0][1]:
                            r[ni] = -r[i]
                            visited[ni] = visited[i] + 1
                            end += 1
                            q[end] = ni
    # print(r)
    # print(visited)

    for k in range(4):
        if r[k] == 1:
            temp = [magnets[k][-1]]
            temp_magnet = temp + magnets[k][:-1]
            magnets[k] = temp_magnet
        elif r[k] == -1:
            temp = [magnets[k][0]]
            temp_magnet = magnets[k][1:] + temp
            magnets[k] = temp_magnet
    # print(magnets)


di = [1, -1]

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    magnets = [list(map(int, input().split())) for _ in range(4)]
    # print(magnets)
    for k in range(K):
        magnet_number, rotation = map(int, input().split())
        rotate(magnet_number, rotation)

    score = 0
    for k in range(4):
        if k == 0:
            score += magnets[k][0]
        elif k == 1:
            score += magnets[k][0]*2
        elif k == 2:
            score += magnets[k][0]*4
        else:
            score += magnets[k][0]*8
    print('#{} {}'.format(tc, score))