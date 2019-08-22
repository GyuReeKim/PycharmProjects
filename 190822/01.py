# 파리 퇴치

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    for i in range(0, N-K+1):
        for j in range(0, N-K+1):
            s = 0
            for r in range(i, i+K):
                for c in range(j, j+K):
                    s += fly[r][c]
            if maxV < s:
                maxV = s
    print('#{} {}'.format(tc, maxV))

# x자 모양의 파리채
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    for i in range(0, N-K+1):
        for j in range(0, N-K+1):
            s = 0
            for m in range(K):
                s += fly[i + m][j + m]  # 오른쪽 아래 방향
                s += fly[i + m][j + K - 1 - m]  # 왼쪽 아래 방향
            # K가 홀수인 경우 가운데 원소가 두번 더해지므로
            if K % 2 == 1:  # 홀수일 경우
                s -= fly[i + K // 2][j + K // 2]  # 중복된 가운데 한개를 빼줌
            if maxV < s:
                maxV = s
    print('#{} {}'.format(tc, maxV))