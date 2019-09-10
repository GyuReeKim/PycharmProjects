# 이진 힙
# 푸는 중...


# def f(n):



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    parent = [0 for i in range(N+1)]
    print(parent)
    node = list(map(int, input().split()))
    for i in range(N):
        if parent[1] < node[i]