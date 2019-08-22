# 모자이크 모양의 파리채

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    for i in range(0, N-K+1):
        for j in range(0, N-K+1):
            s = 0
            # s_fly = []
            for n in range(i, i+K):
                for m in range(j, j+K):
                    if i % 2 == 0 and j % 2 == 0:
                        if n % 2 == 0 and m % 2:
                            s += fly[m][n]
                            # s_fly.append(fly[m][n])
                        elif n % 2 and m % 2 == 0:
                            s += fly[m][n]
                            # s_fly.append(fly[m][n])
                    elif i % 2 == 0 and j % 2:
                        if n % 2 == 0 and m % 2 == 0:
                            s += fly[m][n]
                            # s_fly.append(fly[m][n])
                        elif n % 2 and m % 2:
                            s += fly[m][n]
                            # s_fly.append(fly[m][n])
                    elif i % 2 and j % 2 == 0:
                        if n % 2 and m % 2:
                            s += fly[m][n]
                            # s_fly.append(fly[m][n])
                        elif n % 2 == 0 and m % 2 == 0:
                            s += fly[m][n]
                            # s_fly.append(fly[m][n])
                    elif i % 2 and j % 2:
                        if n % 2 and m % 2 == 0:
                            s += fly[m][n]
                            # s_fly.append(fly[m][n])
                        elif n % 2 == 0 and m % 2:
                            s += fly[m][n]
                            # s_fly.append(fly[m][n])

            # print(s_fly)
            if maxV < s:
                maxV = s
    print('#{} {}'.format(tc, maxV))