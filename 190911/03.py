# 상호의 배틀필드
import pprint


def U(i, j):
    global board
    board[i][j] = '.'
    ni = i - 1
    # print(ni)
    if ni >= 0:
        if board[ni][j] == '.':
            board[ni][j] = '^'
        else:
            board[i][j] = '^'
    else:
        board[i][j] = '^'


def D(i, j):
    global board
    board[i][j] = '.'
    ni = i + 1
    if ni < H:
        if board[ni][j] == '.':
            board[ni][j] = 'v'
        else:
            board[i][j] = 'v'
    else:
        board[i][j] = 'v'


def L(i, j):
    global board
    board[i][j] = '.'
    nj = j - 1
    if nj >= 0:
        if board[i][nj] == '.':
            board[i][nj] = '<'
        else:
            board[i][j] = '<'
    else:
        board[i][j] = '<'


def R(i, j):
    global board
    board[i][j] = '.'
    nj = j + 1
    if nj < W:
        if board[i][nj] == '.':
            board[i][nj] = '>'
        else:
            board[i][j] = '>'
    else:
        board[i][j] = '>'


def S(i, j):
    global n
    global board
    direction = ['^', 'v', '<', '>']
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    for k in range(4):
        if k < 2:
            if board[i][j] == direction[k]:
                for l in range(1, H):
                    ni = i + di[k]*l
                    nj = j + dj[k]*l
                    if ni >= 0 and ni < H and nj >= 0 and nj < W:
                        # print(n, ni, nj)
                        if board[ni][nj] == '#':
                            break
                        elif board[ni][nj] == '*':
                            board[ni][nj] = '.'
                            break
        else:
            if board[i][j] == direction[k]:
                for l in range(1, W):
                    ni = i + di[k]*l
                    nj = j + dj[k]*l
                    if ni >= 0 and ni < H and nj >= 0 and nj < W:
                        # print(n, ni, nj)
                        if board[ni][nj] == '#':
                            break
                        elif board[ni][nj] == '*':
                            board[ni][nj] = '.'
                            break


T = int(input())
for tc in range(1, T+1):
    H, W = list(map(int, input().split()))
    board = [list(input()) for _ in range(H)]
    N = int(input())
    command = input()
    # pprint.pprint(board, indent=4, width=70)

    startI = 0
    startJ = 0
    for n in range(N):
        for i in range(H):
            for j in range(W):
                if board[i][j] == '^' or board[i][j] == 'v' or board[i][j] == '<' or board[i][j] == '>':
                    startI = i
                    startJ = j
        if command[n] == 'U':
            U(startI, startJ)
            # break
        elif command[n] == 'D':
            D(startI, startJ)
            # break
        elif command[n] == 'L':
            L(startI, startJ)
            # break
        elif command[n] == 'R':
            R(startI, startJ)
            # break
        else:
            S(startI, startJ)
            # break
        # print(n)
        # pprint.pprint(board, indent=4, width=70)

    print('#{}'.format(tc), end=' ')
    for h in range(H):
        print(''.join(board[h]))
