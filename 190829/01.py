# 부먹 왕국의 차원 관문

T = int(input())
for tc in range(1, T+1):
    N, D = list(map(int, input().split()))
    kingdom = [1] + list(map(int, input().split())) + [1]
    # print(kingdom)

    cnt = 0
    last = N+1
    for i in range(N+1, 0, -1):
        if i == last:
            for j in range(1, D+1):
                if kingdom[i-j] == 1:
                    last = i-j
                    if i-j == 0:
                        break
            if last == i and kingdom[i-D] == 0:
                kingdom[i-D] = 1
                cnt += 1
                last = i-D
            #     print(last)
            # print(kingdom)
    print('#{} {}'.format(tc, cnt))







    #
    #         if i == last:
    #             if kingdom[i-j] == 1:
    #                 last = i-j
    #                 print(last)
    #                 if i-j == 0:
    #                     break
    #                 if last == i and kingdom[i-j] == 0:
    #                     cnt += 1
    #                     last = i-j
    #                     kingdom[last] += 1
    #                     print(last)
    # print(cnt)

