# 재미있는 오셀로 게임
# 다시 풀기

import pprint

def neighbor(i, j):
    global N
    global arr
    global r
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]

    for k in range(8):
        ni = i + di[k]
        nj = j + dj[k]
        if ni >= 0 and ni < N and nj >= 0 and nj < N:
            if arr[ni][nj] != r:
                return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    for m in range(M):
        y, x, r = list(map(int, input().split()))

        arr = [[0]*N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if (i == N//2 and j == N//2) or (i == N//2-1 and j == N//2-1):
                    arr[i][j] = 2
                elif (i == N//2 and j == N//2-1) or (i == N//2-1 and j == N//2):
                    arr[i][j] = 1
        # print(arr)

        for i in range(N):
            for j in range(N):
                if neighbor(y-1, x-1) == 1:
                    arr[y-1][x-1] = r
        print()
        pprint.pprint(arr, indent=4, width=N*10)