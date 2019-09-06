# 재미있는 오셀로 게임
# import pprint


def find(i, j, r):
    global N
    global arr
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]

    for k in range(8):
        cnt_r = 0
        for l in range(1, N):
            ni = i + di[k]*l
            nj = j + dj[k]*l
            if ni >= 0 and ni < N and nj >= 0 and nj < N:
                if arr[ni][nj] == 0:
                    break
                elif arr[ni][nj] == r:
                    if cnt_r == l-1:
                        for c in range(1, cnt_r+1):
                            arr[i + di[k]*c][j + dj[k]*c] = r
                else:
                    cnt_r += 1


T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [[0]*N for _ in range(N)]

    arr[N//2-1][N//2] = 1
    arr[N//2][N//2-1] = 1
    arr[N//2-1][N//2-1] = 2
    arr[N//2][N//2] = 2
    # pprint.pprint(arr, indent=4, width=N*10)

    for m in range(M):
        y, x, r = list(map(int, input().split()))
        arr[x-1][y-1] = r
        find(x-1, y-1, r)
        # pprint.pprint(arr, indent=4, width=N*10)

    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j] == 2:
                white += 1
    print('#{} {} {}'.format(tc, black, white))