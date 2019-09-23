# 최소 비용
# 푸는중

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    # print(board)
    D = [[1000000]*N for _ in range(N)]
    D[0][0] = 0
    print(D)
    U = [[0]*N for _ in range(N)]
    print(U)