# fibonacci

# def fibo1(n):
#     global memo
#     if n >= 2 and len(memo) <= n:
#         memo.append(fibo1(n-1) + fibo1(n-2))
#     return memo[n]
#
# memo = [0, 1]

# N = 4
# print(fibo1(N))

def fibo(n):
    global memo
    if n >= 2 and memo[n] == 0: # 아직 fibo(n)이 계산되지 않은 경우
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n] # fibo(n)이 계산되어 있으면 리턴

N = 7
memo = [0]*(N+1)
memo[0] = 0
memo[1] = 1
print(fibo(N))
print()