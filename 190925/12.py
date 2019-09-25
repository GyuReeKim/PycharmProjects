# 이전 순열

N = int(input())
p = list(map(int, input().split()))

j = N-1
i = j-1
while i >= 0:
    if p[i] > p[j]:
        break
    i -= 1
    j -= 1
if i == -1:
    print(-1)
else:
    k = N-1
    while p[k] > p[i]:
        k -= 1
    p[i], p[k] = p[k], p[i]
    p = p[:i+1] + p[i+1:][::-1]
    result = [str(p[i]) for i in range(N)]
    print(' '.join(result))