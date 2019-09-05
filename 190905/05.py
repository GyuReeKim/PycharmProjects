# 미로의 거리

def find(i, j):
    global maze
    global N
    global cnt
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    if maze[i][j] == '3':
        cnt += 1
        return 1
    else:
        maze[i][j] = '1'
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            cnt = 0
            if ni >= 0 and ni < N and nj >= 0 and nj < N:
                if maze[ni][nj] != '1':
                    if find(ni, nj) == 1:
                        cnt += 1
                        return 1
        return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    # print(maze)

    startI = 0
    startJ = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                startI = i
                startJ = j
    if find(startI, startJ) == 0:
        print('#{} 0'.format(tc))
    else:
        print('#{} {}'.format(tc, cnt-2))