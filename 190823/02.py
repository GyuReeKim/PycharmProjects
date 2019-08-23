# 시험2
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(0, N-K+1):
        for j in range(0, M-K+1):
            # s = 0
            # for p in range(K):
            #     s += arr[i][j+p] # 부분 배열의 맨 윗줄
            #     s += arr[i+K-1][j+p] # 맨 아랫줄
            #     s += arr[i+p][j] # 왼쪽 열
            #     s += arr[i][j+p] # 오른쪽 열
            # s -= arr[i][j]
            # s -= arr[i+K-1][j]
            # s -= arr[i][j+K-1]
            # s -= arr[i+K-1][j+K-1]
            # if maxV < s:
            #     maxV = s

            s = 0
            for r in range(i, i+K):
                for c in range(j, j+K):
                    if r == i or r == i+K-1 or c == j or c == j+K-1:
                        s += arr[r][c]
            if maxV <s:
                maxV = s
                
    print('#{} {}'.format(tc, maxV))