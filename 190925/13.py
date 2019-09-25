# 배열 변형 문제

T = 10
for tc in range(1, T+1):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    p = [1000000 for i in range(30)]
    for k in range(30):
        s1 = 0
        s2 = 0
        for i in range(100):
            s1 += abs(arr[i][i] - (k+1))
            s2 += abs(arr[i][100-(i+1)] - (k+1))
            r = 0
            c = 0
            for j in range(100):
                r += abs(arr[i][j] - (k+1))
                c += abs(arr[j][i] - (k+1))
            if r < p[k]:
                p[k] = r
            if c < p[k]:
                p[k] = c
        if s1 < p[k]:
            p[k] = s1
        if s2 < p[k]:
            p[k] = s2
    # print(p)

    minV = 1000000
    idxI = 0
    for k in range(30):
        if p[k] < minV:
            minV = p[k]
            idxI = k+1
    print('#{} {} {}'.format(tc, minV, idxI))