import sys
sys.stdin = open('input.txt', 'r')


def square(arr):
    for i in range(3):
        for j in range(3):
            add = 0
            for r in range(3):
                for c in range(3):
                    add += arr[i*3+r][j*3+c]
            if add != 45:
                return 0
    return 1


def row(arr):
    for i in range(9):
        add = 0
        for j in range(9):
            add += arr[i][j]
        if add != 45:
            return 0
    return 1


def col(arr):
    for i in range(9):
        add = 0
        for j in range(9):
            add += arr[j][i]
        if add != 45:
            return 0
    return 1


T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    # for i in range(3):
    #     for j in range(3):
    #         add = 0
    #         for r in range(3):
    #             for c in range(3):
    #                 add += sudoku[i*3+r][j*3+c]
    #         print(add)

    result = 1
    if square(sudoku) == 0 or row(sudoku) == 0 or col(sudoku) == 0:
        result = 0

    print('#{} {}'.format(tc, result))