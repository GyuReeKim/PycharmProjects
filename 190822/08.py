# 파리X

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    for i in range(0, N-K+1):
        for j in range(0, N-K+1):
            s = 0
            for r in range(i, i+K):
                for c in range(j, j+K):
                    if r-i == c-j or r+c-i-j == K-1:
                        s += fly[r][c]
            if maxV < s:
                maxV = s
    print('#{} {}'.format(tc, maxV))