# 증가 구간의 최대 길이
N = 7
A = [4, 5, 1, 2, 3, 2, 1]


maxV = 1
l = 1
for i in range(1, N):
    if A[i-1] < A[i]: # 증가 구간인 경우
        l += 1 # 이전 까지의 증가 구간 길이 + 1
        if maxV < l:
            maxV = l
    else: # 증가 구간이 아니면
        l = 1

print(maxV)