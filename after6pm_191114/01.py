# 백준 11559번 Puyo Puyo
# 푸는중 (답 틀림)

import pprint
import sys
sys.stdin = open('01.txt', 'r')


def puyo_delete(board, visited):
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                board[i][j] = '.'


def puyo_move(board):
    for j in range(M):
        temp = []
        blank_count = 0
        for i in range(N):
            if board[i][j] != '.':
                temp += [board[i][j]]
            else:
                blank_count += 1
        temp = ['.']*blank_count + temp

        for i in range(N):
            board[i][j] = temp[i]
        # print('move', board)


def color_4_up(i, j, color):
    global board
    # color = -1
    # for k in range(len(colors)):
    #     if board[i][j] == colors[k]:
    #             color = k

    q = ['']*N*M
    visited = [[0 for b in range(M)] for a in range(N)]
    start, end = -1, -1

    visited[i][j] = 1
    end += 1
    q[end] = [i, j]

    while start != end:
        start += 1
        si, sj = q[start][0], q[start][1]
        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                if board[ni][nj] == colors[color]:
                    visited[ni][nj] = 1
                    end += 1
                    q[end] = [ni, nj]
    # print(visited)
    visit_count = 0
    for r in range(N):
        for c in range(M):
            if visited[r][c] == 1:
                visit_count += 1
    # print(visit_count)
    if visit_count >= 4:
        # 방문표시된 board 제거
        puyo_delete(board, visited)
        # print('after delete', board)
        # 아래로 이동
        puyo_move(board)
        # print(board)
        return 1
    return 0



di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = 12
M = 6

board = [list(input()) for _ in range(12)]
# print(board)

colors = ['R', 'G', 'P', 'Y']

cnt = 0
while True:
    turn_end = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != '.':
                color = -1
                for k in range(len(colors)):
                    if board[i][j] == colors[k]:
                        color = k
                # print(colors[color])
                # color가 4개 이상 연속되어있는지 확인해야한다.
                # print(i, j)
                    if color_4_up(i, j, color) == 1:
                        # cnt += 1
                        turn_end = 1

            if turn_end == 1:
                # print('break')
                break
        if turn_end == 1:
            pprint.pprint(board, indent=4, width=M*10)
            cnt += 1
            # print('break')
            break
    if turn_end == 0:
        break
print(cnt)