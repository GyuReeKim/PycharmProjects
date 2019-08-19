# 종이붙이기

def fibo(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo(n-1) + 2 * fibo(n-2))
    return memo[n]

memo = [1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = int(N/10)
    print('#{} {}'.format(tc, fibo(n)))