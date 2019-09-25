# 백준 - 숫자 정사각형 1051번


def square(i, j):
    global maxV
    for r in range(i+1):
        for c in range(j+1):
            s = 0
            if i-r+1 == j-c+1:
                if rec[r][c] == rec[r][j] == rec[i][c] == rec[i][j]:
                    # print(i, j)
                    s = (i-r+1) * (j-c+1)
            if s > maxV:
                maxV = s


N, M = map(int, input().split())
rec = [list(map(int, input())) for _ in range(N)]
# print(rec)

maxV = 0
for i in range(N):
    for j in range(M):
        square(i, j)
print(maxV)