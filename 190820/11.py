# 파리 퇴치

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))

    arr = [[]*N for a in range(N)]
    # print(arr)

    for n in range(N):
        num = list(map(int, input().split()))
        arr[n] = num
    # print(arr)

    result = []
    for i in range(N-(M-1)):
        for j in range(N-(M-1)):
            add = 0
            for k in range(i, i+M):
                add += sum(arr[k][j:j+M])
                # print(add)
                result.append(add)
    print('#{} {}'.format(tc, max(result)))
