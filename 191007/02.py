# 당근 수확2

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    farm = [0] + list(map(int, input().split()))
    # print(farm)

    cnt = 0
    while len(set(farm)) > 1:
        temp = M
        for i in range(1, N+1):
            if farm[i] < temp:
                temp -= farm[i]
                farm[i] = 0
                if temp <= 0:
                    cnt += i*2
                    break
            else:
                farm[i] -= temp
                temp = 0
                cnt += i*2
                break
        if farm[N] == 0:
            cnt += N*2
        # print(cnt, farm)
    print(f'#{tc} {cnt}')