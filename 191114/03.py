# [모의 SW 역량테스트] 벽돌 깨기
# 푸는중

import pprint
import sys
sys.stdin = open('test.txt', 'r')


def check_top(i, j):
    if block[i][j] != 0:
        if i == 0:
            return 1
        if i - 1 >= 0:
            if block[i-1][j] == 0:
                return 1
    return 0


def check_bomb(i, j, bomb):
    for r in range(H):
        if i - block[i][j] < r < i + block[i][j]:
            bomb[r][j] = 1
    for c in range(W):
        if j - block[i][j] < c < j + block[i][j]:
            bomb[i][c] = 1


def delete_bomb(bomb):
    global copy_block
    copy_block = [[0 for b in range(W)] for a in range(H)]
    for i in range(H):
        for j in range(W):
            if bomb[i][j] == 1:
                copy_block[i][j] = 0
            else:
                copy_block[i][j] = block[i][j]


def block_drop(copy_block):
    for j in range(W):
        temp = []
        zero_count = 0
        for i in range(H):
            if copy_block[i][j] != 0:
                temp += [copy_block[i][j]]
            else:
                zero_count += 1
        temp = [0] * zero_count + temp

        for i in range(H):
            copy_block[i][j] = temp[i]


def block_change(i, j):
    global copy_block, block
    bomb = [[0 for b in range(W)] for a in range(H)]
    check_bomb(i, j, bomb)

    visited = [[0 for b in range(W)] for a in range(H)]
    q = [''] * W * H
    start, end = -1, -1

    visited[i][j] = 1
    end += 1
    q[end] = [i, j]

    while start != end:
        start += 1
        i, j = q[start][0], q[start][1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < H and 0 <= nj < W and visited[ni][nj] == 0 and bomb[ni][nj] == 1:
                check_bomb(ni, nj, bomb)

                visited[ni][nj] = 1
                end += 1
                q[end] = [ni, nj]
    delete_bomb(bomb)
    block_drop(copy_block)
    print(kk, [rr, cc], 'copy_block')
    pprint.pprint(copy_block, indent=4, width=W * 10)

    block = [[0 for b in range(W)] for a in range(H)]
    for r in range(H):
        for c in range(W):
            block[r][c] = copy_block[r][c]

    # pprint.pprint(block, indent=4, width=W * 10)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    block = [list(map(int, input().split())) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            # if check_top(i, j) == 1:
            if [i, j] == [1, 1]:
                for k in range(N):
                    kk = k
                    rr = i
                    cc = j
                    if k == 0:
                        block_change(i, j)
                        print(k, 'block')
                        pprint.pprint(block, indent=4, width=W * 10)
                    else:
                        temp_block = [[0 for b in range(W)] for a in range(H)]
                        for r in range(H):
                            for c in range(W):
                                temp_block[r][c] = block[r][c]

                        for r in range(H):
                            for c in range(W):
                                if check_top(r, c) == 1:
                                    rr = r
                                    cc = c
                                    block_change(r, c)
                        print(k, 'block')
                        pprint.pprint(block, indent=4, width=W * 10)
                        block = [[0 for b in range(W)] for a in range(H)]
                        for x in range(H):
                            for y in range(W):
                                block[x][y] = temp_block[x][y]
                        print(k, 'return_block')
                        pprint.pprint(block, indent=4, width=W * 10)
