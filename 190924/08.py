# 구간 합


def f(a, b, c, d):
    R = c - a + 1
    C = d - b + 1
    s = 0
    for i in range(R):
        for j in range(C):
            s += arr[a+i][b+j]
    return s


N = 5
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

result = 0
for i in range(N-1):
    for j in range(N-1):
        a = f(0, 0, i, j)
        b = f(0, j+1, i, N-1)
        c = f(i+1, 0, N-1, j)
        d = f(i+1, j+1, N-1, N-1)
        if a == b == c == d:
            result = 1
            break
    if result == 1:
        break
print(result)