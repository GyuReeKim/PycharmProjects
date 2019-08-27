T = int(input())
for tc in range(1, T+1):
    N, M, K = list(map(int, input().split()))

    arr = [[0]*M for _ in range(N)]
    max_c = 0
    for k in range(K):
        n1, m1, n2, m2, c = list(map(int, input().split()))
        if k == 0:
            for i in range(N):
                for j in range(M):
                    if n1 <= i <= n2 and m1 <= j <= m2:
                        if c > arr[i][j]:
                            arr[i][j] = c
                            if c > max_c:
                                max_c = c
        status = ''
        if k != 0:
            if max_c > c:
                for i in range(N):
                    for j in range(M):
                        if n1 <= i <= n2 and m1 <= j <= m2:
                            if arr[i][j] > c:
                                status = 'duplicated'
        if k != 0:
            if status != 'duplicated':
                for i in range(N):
                    for j in range(M):
                        if n1 <= i <= n2 and m1 <= j <= m2:
                            if c > arr[i][j]:
                                arr[i][j] = c
                                if c > max_c:
                                    max_c = c

    colors = []
    for color in range(11):
        count = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == color:
                    count += 1
        colors.append(count)
    print('#{} {}'.format(tc, max(colors)))