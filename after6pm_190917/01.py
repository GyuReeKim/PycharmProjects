# 백준 - 브루트 포스 - 부분수열의 합 (1182번)

# 백준 input에 사용
import sys
input = lambda :sys.stdin.readline().rstrip()

N, S = list(map(int, input().split()))
num = list(map(int, input().split()))

cnt = 0
for i in range(1, 1<<N):
    add = 0
    for j in range(N):
        if i & (1<<j):
            add += num[j]
    if add == S:
        cnt += 1
print(cnt)