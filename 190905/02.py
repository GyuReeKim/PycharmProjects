# 스도쿠 검증


def square(sudoku):
    for i in range(3):
        for j in range(3):
            add = 0
            for r in range(3):
                for c in range(3):
                    add += sudoku[r + i*3][c + j*3]
            if add != 45:
                return 0
    return 1


def row(sudoku):
    for i in range(9):
        add = 0
        for j in range(9):
            add += sudoku[i][j]
        if add != 45:
            return 0
    return 1


def col(sudoku):
    for i in range(9):
        add = 0
        for j in range(9):
            add += sudoku[j][i]
        if add != 45:
            return 0
    return 1


T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    # print(sudoku)

    if square(sudoku) == 1 and row(sudoku) == 1 and col(sudoku) == 1:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))