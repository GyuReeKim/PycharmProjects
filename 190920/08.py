# 6일차 - 그룹 나누기
# 푸는중


# def f(N):


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    group = list(map(int, input().split()))
    visited = [0]*(N+1)
    adj = [[0]*(N+1) for _ in range(N+1)]
    for i in range(M):
        n1, n2 = group[i*2], group[i*2+1]
        adj[n1][n2] = 1
        adj[n2][n1] = 1
    print()