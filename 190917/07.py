# 백준 11053번
# 풀이중...

N = int(input())
A = list(map(int, input().split()))

maxC = 0
for i in range(N):
    print(A[i:])
    maxV = 0
    cnt = 0
    for j in range(i, N):
        if A[j] > maxV:
            maxV = A[j]
            cnt += 1
    if cnt > maxC:
        maxC = cnt
print(maxC)