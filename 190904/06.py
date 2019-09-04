# 어디에 단어가 들어갈 수 있을까
# import pprint


def right(i, j):
    global puzzle
    global M

    length = 1
    # nx = i + 0
    ny = j - 1
    for l in range(1, N):
        # ni = i + 0*l
        nj = j + 1*l
        if i >= 0 and i < N and nj >= 0 and nj < N:
            if j == 0:
                if puzzle[i][nj] == 0:
                    break
                else:
                    length += 1
            else:
                if puzzle[i][ny] != 1:
                    if puzzle[i][nj] == 0:
                        break
                    else:
                        length += 1
    # print('right_length: {}'.format(length))
    if length == M:
        return 1
    return 0


def down(i, j):
    global puzzle
    global M

    length = 1
    nx = i - 1
    # ny = j + 0
    for l in range(1, N):
        ni = i + 1*l
        # nj = j + 0*l
        if ni >= 0 and ni < N and j >= 0 and j < N:
            if i == 0:
                if puzzle[ni][j] == 0:
                    break
                else:
                    length += 1
            else:
                if puzzle[nx][j] != 1:
                    if puzzle[ni][j] == 0:
                        break
                    else:
                        length += 1
    # print('down_length: {}'.format(length))
    if length == M:
        return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # pprint.pprint(puzzle, indent=4, width=N*10)

    cnt = 0
    startI = 0
    startJ = 0
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 1:
                startI = i
                startJ = j
                # print()
                # print([startI, startJ])
                # print('right: {}'.format(right(startI, startJ)))
                # print('down: {}'.format(down(startI, startJ)))
                if right(startI, startJ) == 1:
                    cnt += 1
                if down(startI, startJ) == 1:
                    cnt += 1
    print('#{} {}'.format(tc, cnt))