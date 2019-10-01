# [모의 SW 역량테스트] 무선 충전
# A 충전기 리스트, B 충전기 리스트 만든 후 겹치는 범위 이중for문으로..
# A = [1, 2], B = [2, 3]
# A = 1 1 2 2
# B = 2 3 2 3
# 충전량
import pprint


def move(ai, aj, bi, bj, mA, mB):
    global AI, AJ, BI, BJ
    di = [0, -1, 0, 1, 0]
    dj = [0, 0, 1, 0, -1]
    for k in range(5):
        if k == mA:
            AI = ai + di[k]
            AJ = aj + dj[k]
        if k == mB:
            BI = bi + di[k]
            BJ = bj + dj[k]


def charge(i, j, k, ck):
    global arr
    for r in range(1, 11):
        for c in range(1, 11):
            if abs(r-i) + abs(c-j) <= ck:
                if k not in arr[r][c]:
                    arr[r][c] += k


T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    moveA = list(map(int, input().split()))
    moveB = list(map(int, input().split()))
    charger = [list(map(int, input().split())) for _ in range(A)]
    print(charger)

    arr = [['']*11 for _ in range(11)]

    for i in range(11):
        for j in range(11):
            for k in range(A):
                if i == charger[k][0] and j == charger[k][1]:
                    arr[i][j] += str(k)
                    charge(i, j, str(k), charger[k][2])
    pprint.pprint(arr, indent=4, width=110)

    AI = 1
    AJ = 1
    BI = 10
    BJ = 10
    for m in range(M):
        move(AI, AJ, BI, BJ, moveA[m], moveB[m])
        print(AI, AJ, BI, BJ)