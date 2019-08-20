# 봉우리

# N = 7
N = 10
# A = [1, 2, 1, 2, 1, 2, 1]
A = [7, 2, 3, 4, 1, 2, 5, 4, 5, 6]

slope = 0
cnt = 0
size = 0
maxV = 0
for i in range(1, N):
    if A[i-1] > A[i]:
        if slope == 1: # 내리막이고 이전까지 오르막이면
            cnt += 1 # 오르막 -> 내리막인 봉우리이므로
            slope = 0
            if maxV < size:
                maxV = size
            size = 1
    else:
        slope = 1
    if size > 0:
        size += 1
if cnt < 2:
    maxV = 0

print(cnt, maxV)
