T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # for n in range(N):
    #     A, B = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(N)]
    print(ab)
    P = int(input())
    # for p in range(P):
    #     C = int(input())
    c = [int(input()) for _ in range(P)]
    print(c)

    arr = [0]*P
    # print(arr)

    for i in range(N):
        for j in range(P):
            if ab[i][0] <= c[j] <= ab[i][-1]:
                arr[j] += 1
    print(arr)

    arr = ' '.join([str(arr[p]) for p in range(P)])
    # print(arr)

    print(f'#{tc} {arr}')