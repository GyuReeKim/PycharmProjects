# 구간 자르기

N = 5
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

for i in range(N-1):
    for j in range(N-1):
        s1 = [[0]*(j+1-0) for _ in range(i+1-0)]
        for r in range(0, i+1):
            for c in range(0, j+1):
                s1[r][c] = arr[r][c]
        print(s1)
        s2 = [[0]*(N-(j+1)) for _ in range(i+1-0)]
        for r in range(0, i+1):
            for c in range(j+1, N):
                s2[r][c-(j+1)] = arr[r][c]
        print(s2)
        s3 = [[0]*(j+1-0) for _ in range(N-(i+1))]
        for r in range(i+1, N):
            for c in range(0, j+1):
                s3[r-(i+1)][c] = arr[r][c]
        print(s3)
        s4 = [[0]*(N-(j+1)) for _ in range(N-(i+1))]
        for r in range(i+1, N):
            for c in range(j+1, N):
                s4[r-(i+1)][c-(j+1)] = arr[r][c]
        print(s4)