def fly(N, X, H, board):
    for i in range(X, N+2*X):
        for j in range(X, N+2*X):
            if abs(H[i]-H[i-j]) > 1 or abs(H[i]-H[i+j]) > 1:
                return -1
            elif H



T = int(input())
for tc in range(1, T+1):
    N, X = list(map(int, input().split()))
    H = [[0]*(N+2*X) for _ in range(X)]
    H += [[0]*X + list(map(int, input().split())) + [0]*X for _ in range(N)]
    H += [[0]*(N+2*X) for _ in range(X)]
    print(H)

    board = [[0]*(N+2*X) for _ in range(N+2*X)]
    print(board)


