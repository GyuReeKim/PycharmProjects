# 부분집합

N = 4
A = [1, 2, 3, 4]

for i in range(1<<N):
    res = []
    for j in range(N):
        if i & (1<<j) != 0:
            res.append(A[j])
    print(res)