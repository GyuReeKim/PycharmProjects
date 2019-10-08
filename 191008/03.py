# 농작물 수확하기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    K = N//2
    all = 0
    for i in range(N):
        res = 0
        if i <= K:
            for j in range(K-i, K+i+1):
                res += farm[i][j]
        else:
            for j in range(K-(N-1-i), K+(N-1-i)+1):
                res += farm[i][j]
        all += res
    print('#{} {}'.format(tc, all))