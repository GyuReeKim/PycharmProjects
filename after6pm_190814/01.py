## N과 M이 주어진다. N개의 정수가 입력될 때 M보다 큰 수의 개수를 출력하시오
### N과 N개의 정수가 한 줄에 입력된다. N개의 정수 중 홀수의 개수를 출력하시오

# N개의 정수를 입력받아 정수로 리스트에 저장
N = int(input())
N, M = map(int, input().split())

###
A = list(map(int, input().split()))

# 1
count = 0
for a in A:
    if a % 2 == 0:
        count += 1
print(count)

# 1 풀이
count = 0 # 짝수의 개수 기록
for i in range(0, N): # 탐색 구간, 0부터 N개
    if A[i] % 2 == 0: # 각 숫자에 대해(리스트의 각 원소에 대해)
        count = count + 1
print(count)

##
count = 0
for i in range(0, N):
    if A[i] > M:
        count = count + 1
print(count)

###
N = A[0]
count = 0
# for i in range(1, A[0]+1):
for i in range(1, N+1): # 탐색구간
    if A[i] % 2:
        count = count + 1
print(count)

