# 6일차 - 연산


def bfs(N, M):
    f = -1 # q의 연산이 필요한 값의 인덱스
    b = -1 # q의 마지막 인덱스
    q = [0] * 1000000
    visited = [0] * 1000001

    # N을 q의 마지막 인덱스에 넣어주기
    b += 1
    q[b] = N # push()
    visited[N] = 1

    # N과 M이 같을 때
    if N == M:
        return visited[N] - 1

    # 모든 연산이 끝났을 때
    while f != b:
        f += 1 # 연산이 필요한 값의 인덱스로 f를 옮기기
        x = q[f] # pop()
        for nx in [x+1, x-1, x*2, x-10]:
            if 0 < nx <= 1000000 and visited[nx] == 0: # nx는 백만 이하의 자연수, 연산 중에 등장하지 않았을 경우
                visited[nx] = visited[x] + 1 # visited에 연산횟수를 넣어주기
                # 원하는 값이 나왔다면
                if nx == M:
                    return visited[nx] - 1
                else:
                    b += 1 # 마지막 인덱스의 위치 옮겨주기
                    q[b] = nx # push()

    # 결과를 찾지 못했을 때
    return -1


T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    print('#{} {}'.format(tc, bfs(N, M)))