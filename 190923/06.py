# 최소 이동 거리
# 푸는중

def rep(n):
    while p[n] != n:
        n = p[n]
    return n


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    print(edge)
    p = [i for i in range(V+1)] #  대표원소 배열
    print(p)
    d = [i if i == 0 else 1000000 for i in range(V+1)]
    print(d)
    v = [0 for i in range(V+1)]
    print(v)