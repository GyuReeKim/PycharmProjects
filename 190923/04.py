# 최소 비용
# 시간 초과


def f(i, j, d, c, diff):
    global minV
    global minD
    global cnt
    cnt += 1
    if c >= minV:
        return
    elif diff > minD:
        return
    elif d == (N-1)*2:
        # print(c)
        if c < minV:
            minV = c
        if diff < minD:
            minD = diff
    else:
        if i+1 < N:
            if board[i][j] != board[i+1][j]:
                f(i+1, j, d+1, c + board[i+1][j] + 1, diff + 1)
            else:
                f(i+1, j, d+1, c + 1, diff)
        if j+1 < N:
            if board[i][j] != board[i][j+1]:
                f(i, j+1, d+1, c + board[i][j+1] + 1, diff + 1)
            else:
                f(i, j+1, d+1, c + 1, diff)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    # print(board)
    minV = 1000000
    minD = 1000000
    cnt = 0
    f(0, 0, 0, 0, 0)
    print('#{} {}'.format(tc, minV))
    print(cnt)