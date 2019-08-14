# 바로 왼쪽의 숫자보다 큰 숫자의 개수는?
## 바로 오른쪽의 숫자보다 큰 숫자의 개수는?
N = int(input())
A = list(map(int, input().split()))

# 2
count = 0
for i in range(1, N): # 탐색구간
    if A[i-1] < A[i]:
        count = count + 1
print(count)

##
count = 0
for i in range(0, N-1): # 탐색구간
    if A[i+1] < A[i]:
        count = count + 1
print(count)


