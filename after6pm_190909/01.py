# 수의 새로운 연산
# Runtime error

# import pprint


def point(k):
    global N
    for i in range(1, N+1):
        for j in range(1, N-i+2):
            if arr[i-1][j-1] == k:
                x = j
                y = i
                return [y, x]


N = 10
arr = [[0]*(N-_) for _ in range(N)]

for i in range(1, N+1):
    for j in range(1, N-i+2):
        arr[i-1][j-1] = ((j+i-1)*(j+i))//2 - (i-1)
# pprint.pprint(arr, indent=4, width=N*10)

T = int(input())
for tc in range(1, T+1):
    p, q = list(map(int, input().split()))

    first = point(p)
    second = point(q)

    for i in range(1, N+1):
        for j in range(1, N-i+2):
            if i == first[0] + second[0] and j == first[-1] + second[-1]:
                print('#{} {}'.format(tc, arr[i-1][j-1]))