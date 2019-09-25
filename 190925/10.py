# 다음 순열
# 시간초과


def check(i, j):
    global result
    while p[i] > p[j]:
        if i == 0:
            return -1
        i -= 1
        j -= 1
    k = N-1
    while p[k] < p[i]:
        k -= 1
    p[i], p[k] = p[k], p[i]
    result = p[:i+1] + p[i+1:][::-1]
    return 1


N = int(input())
p = list(map(int, input().split()))
result = []
# print(p)
j = N-1
i = j-1
# print(check(i, j))
if check(i, j) == 1:
    for k in range(N):
        print(result[k], end=' ')
else:
    print(-1)


# check = 1
# while p[i] > p[j]:
#     if i == 0:
#         check = 0
#         break
#     i -= 1
#     j -= 1
# if check == 1:
#     k = N-1
#     while p[k] < p[i]:
#         k -= 1
#     p[i], p[k] = p[k], p[i]
#     left = p[:i+1]
#     right = p[i+1:]
#     res = left + right[::-1]
#     result = [str(res[i]) for i in range(N)]
#     print(' '.join(result))
# else:
#     print(-1)