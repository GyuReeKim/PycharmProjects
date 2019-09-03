# 재미있는 오셀로 게임
# 다시 풀기
# import pprint


def neighbor(i, j):
    global N
    global arr
    global r

    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]

    result = []
    for k in range(8):
        d = 0
        for l in range(2, N):
            ni = i + di[k]*l
            nj = j + dj[k]*l
            if ni >= 0 and ni < N and nj >= 0 and nj < N:
                if arr[i + di[k]][j + dj[k]] != r and arr[i + di[k]][j + dj[k]] != 0:
                    if arr[ni][nj] == 0:
                        break
                    elif arr[ni][nj] == r:
                        d = 1
                        # result.append(k)
        if d == 1:
            result.append(k)
    # print(result)
    return result


def change(i, j, direction):
    global N
    global arr
    global r
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]

    for k in range(8):
        if k in direction:
            for l in range(1, N):
                ni = i + di[k]*l
                nj = j + dj[k]*l
                if ni >= 0 and ni < N and nj >= 0 and nj < N:
                    if arr[ni][nj] == r:
                        break
                    elif arr[ni][nj] != 0:
                        arr[ni][nj] = r
    return arr


T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [[0]*N for _ in range(N)]

    arr[N//2][N//2] = 2
    arr[N//2-1][N//2-1] = 2
    arr[N//2][N//2-1] = 1
    arr[N//2-1][N//2] = 1

    for m in range(M):
        x, y, r = list(map(int, input().split()))

        arr[y-1][x-1] = r
        direction = neighbor(y-1, x-1)
        # print(direction)
        arr = change(y-1, x-1, direction)
        # pprint.pprint(arr, indent=4, width=N*10)

    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt1 += 1
            elif arr[i][j] == 2:
                cnt2 += 1
    print('#{} {} {}'.format(tc, cnt1, cnt2))