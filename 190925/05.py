# 백준 - 다음 순열
# 런타임 에러


def perm(n, k):
    global result
    if n == k:
        result += p
    else:
        for i in range(k):
            if used[i] == 0:
                used[i] = 1
                # print(used)
                p[n] = a[i]
                perm(n+1, k)
                used[i] = 0


N = int(input())
num = list(map(int, input().split()))
a = [i+1 for i in range(N)]
used = [0]*N
p = [0]*N
result = []
perm(0, N)
# print(result)
for i in range(len(result)//4):
    if i == (len(result)//4 - 1):
        print(-1)
    elif result[4*i: 4*(i+1)] == num:
        r = result[4*(i+1): 4*(i+2)]
        r = [str(r[i]) for i in range(4)]
        print(' '.join(r))
        break