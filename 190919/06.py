# N-Queen


def f(i, N):
    global cnt
    print(col, left, right)
    if i == N: # 모든 줄에 퀸을 놓으면
        cnt += 1
    else:
        for j in range(N):
            if col[j] == 0 and right[i+j] == 0 and left[i-j+N-1] == 0:
                # 다른 줄의 j번 열에 퀸이 없어야 하고
                # 왼쪽 대각선과 오른쪽 대각선에 퀸이 없어야 한다.
                # board[i][j] = 1 # 없어도 된다
                col[j] = 1 # 현재 줄에서 j열을 사용함으로 표시
                right[i+j] = 1
                left[i-j+N-1] = 1
                f(i+1, N) # j열에 놓을 수 있으면 다음 줄로 이동
                col[j] = 0
                right[i+j] = 0
                left[i-j+N-1] = 0
                # board[i][j] = 0 # 없어도 된다


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[0]*8 for i in range(8)]
    # print(board)
    cnt = 0
    col = [0]*N
    right = [0]*(2*N-1)
    left = [0]*(2*N-1)
    f(0, N)
    print('#{} {}'.format(tc, cnt))