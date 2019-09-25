# 백준 - 모든 순열
# used 사용


def perm(n, k):
    if n == k:
        result = [str(p[i]) for i in range(N)]
        print(' '.join(result))
    else:
        for i in range(k):
            if used[i] == 0:
                used[i] = 1
                # print(used)
                p[n] = a[i]
                perm(n+1, k)
                used[i] = 0


N = int(input())
a = [i+1 for i in range(N)]
used = [0]*N
p = [0]*N
perm(0, N)