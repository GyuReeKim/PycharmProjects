# 색칠하기
T = int(input())
for tc in range(T):
    arr = [[0]*10 for i in range(10)]
    # print(arr)
    N = int(input())
    for i in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split()))
        for i in range(10):
            for j in range(10):
                if r1 <= i <= r2 and c1 <= j <= c2:
                    if arr[i][j] == 0:
                        arr[i][j] = color
                    else:
                        arr[i][j] += color # color을 칠하면서 count 할 수 있다.
    # print(arr)
    count = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                count += 1
    print('#{} {}'.format(tc+1, count))