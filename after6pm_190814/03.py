N = int(input())
A = list(map(int, input().split()))

# 풀이
for i in range(1, N): # 탐색 구간1 : 처리할 원소의 범위
    # 각 원소 Ai에 대해 할 일
    minV = A[0]
    for j in range(1, i): # Ai의 왼쪽 구간에 대해
        if minV > A[j]:
            minV = A[j]
    print(abs(A[i] - minV), end=' ')