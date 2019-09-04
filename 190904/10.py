# 색칠하기

# import pprint

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    for n in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split()))

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                arr[r][c] += color

    # pprint.pprint(arr, indent=4, width=100)

    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                cnt += 1
    print('#{} {}'.format(tc, cnt))