# 2일차 - 최소합

for t in range(int(input())):
    N = int(input()) +1
    arr = [list(map(int, input().split())) for i in range(N-1)]
    d = [[1000000]*N for i in range(N)]
    d[1][0] = 0
    for i in range(1,N):
        for j in range(1,N):
            d[i][j] = min(d[i-1][j], d[i][j-1]) + arr[i-1][j-1]
    print('#{} {}'.format(t+1, d[N-1][N-1]))