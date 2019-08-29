# 농작물 수확하기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    # print(farm)
    K = N//2

    add = 0
    for i in range(N):
        for j in range(N):
            if j == K:
                for k in range(K+1):
                    if i <= K and i == k:
                        add += sum(farm[i][j-k: j+k+1])
                        # print(i, add)
                    elif i > K and (i+k) == N-1:
                        add += sum(farm[i][j-k: j+k+1])
                        # print(i, add)
    print('#{} {}'.format(tc, add))


