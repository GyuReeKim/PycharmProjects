# [모의 SW 역량테스트] 벽돌 깨기
# 푸는중

import pprint
import sys
sys.stdin = open('test.txt', 'r')


def check_top(i, j):
    if new_block[i][j] != 0:
        if i == 0:
            return 1
        if i - 1 >= 0:
            if new_block[i-1][j] == 0:
                return 1
    return 0


def check_bomb(i, j, bomb):
    # global bomb
    for r in range(H):
        small = i - new_block[i][j]
        big = i + new_block[i][j]
        if small < r < big:
            bomb[r][j] = 1
    for c in range(W):
        small = j - new_block[i][j]
        big = j + new_block[i][j]
        if small < c < big:
            bomb[i][c] = 1
    # print(bomb)


def block_delete(bomb, new_block):
    global copy_block
    copy_block = [[0 for b in range(W)] for a in range(H)]
    for i in range(H):
        for j in range(W):
            if bomb[i][j] == 1:
                copy_block[i][j] = 0
            else:
                copy_block[i][j] = new_block[i][j]
    # print(copy_block)


def block_drop(copy_block):
    for j in range(W):
        temp = []
        zero_count = 0
        for i in range(H):
            if copy_block[i][j] != 0:
                temp += [copy_block[i][j]]
            else:
                zero_count += 1
        temp = [0]*zero_count + temp

        for i in range(H):
            copy_block[i][j] = temp[i]


def block_bomb(i, j, new_block):
    global copy_block

    bomb = [[0 for b in range(W)] for a in range(H)]
    visited = [[0 for b in range(W)] for a in range(H)]
    q = ['']*W*H
    start, end = -1, -1

    check_bomb(i, j, bomb) # 벽돌이 사라지는 범위 확인

    visited[i][j] = 1
    end += 1
    q[end] = [i, j]

    while start != end:
        # print(q)
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
    # pprint.pprint(bomb, indent=4, width=W*10)
    block_delete(bomb, new_block)
    block_drop(copy_block)
    # pprint.pprint(copy_block, indent=4, width=W*10)
    new_block = [[0 for b in range(W)] for a in range(H)]
    for r in range(H):
        for c in range(W):
            new_block[r][c] = copy_block[r][c]
    pprint.pprint(new_block, indent=4, width=W * 10)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    block = [list(map(int, input().split())) for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if [i, j] == [1, 2]:
            # block 복사본 생성
                new_block = [[0 for b in range(W)] for a in range(H)]
                for r in range(H):
                    for c in range(W):
                        new_block[r][c] = block[r][c]

                for k in range(N):
                    # 맨 위의 블록인지 확인
                    print(copy_block)
                    # pprint.pprint(new_block, indent=4, width=W*10)
                    if check_top(i, j) == 1:
                        # 복사본 중 제거 가능한 블럭 제거
                        block_bomb(i, j, new_block)
                        print()