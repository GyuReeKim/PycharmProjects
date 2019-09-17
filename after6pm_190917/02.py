# 백준 - 브루트 포스 - 부분수열의 합 (1182번)


def f(n, k, s):
    global cnt
    if n == k: # 부분집합이 완성되면
        if sum(bit) != 0: # 공집합이 아닌 경우
            t = 0
            for i in range(k): # 부분집합의 합을 구하고
                if bit[i] == 1:
                    t += num[i]
            if t == s: # 부분집합의 합이 S와 같은 경우의 수
                cnt += 1
    else:
        bit[n] = 0
        f(n+1, k, s)
        bit[n] = 1 # 부분집합에 num[n]을 포함
        f(n+1, k, s)


def f2(n, k, s, ts, m): # ts 현재까지 포함시킨 원소의 합, 원소의 개수
    global cnt
    if n == k:
        if m > 0 and ts == s:
            cnt += 1
    else:
        f2(n+1, k, s, ts, m)
        f2(n+1, k, s, ts+num[n], m+1)


N, S = map(int, input().split())
num = list(map(int, input().split()))
bit = [0]*N
cnt = 0
# f(0, N, S)
f2(0, N, S, 0, 0)
print(cnt)