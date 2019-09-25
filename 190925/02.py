# 백준 - 모든 순열


def perm(n, m, k):
    if n == k:
        result = [str(p[i]) for i in range(N)]
        print(' '.join(result))
    else:
        for i in range(n, m):
            p[n], p[i] = p[i], p[n]
            perm(n+1, m, k)
            p[n], p[i] = p[i], p[n]


N = int(input())
p = [i+1 for i in range(N)]
perm(0, N, N)