# 백트래킹
# 합이 10인 부분집합의 개수

def f(i, N, K, s):
    global cnt
    global bit
    global cnt2
    cnt2 += 1
    if s == K: # 나머지 원소를 하나라도 추가하면 K보다 커지므로
        cnt += 1
        return
    elif i == N: # 모든 원소를 고려했지만 합이 K가 아닌경우
        return
    elif s > K:
        return
    else:

        f(i + 1, N, K, s) # i번이 가리키는 값은 부분집합에 포함하지 않음

        f(i + 1, N, K, s + i+1) # i번이 가리키는 값을 부분집합에 포함



N = 10 # 1부터 N까지가 집합의 원소
K = 10 # 부분집합의 합 # 크기를 키우면 원하는 값을 찾을 수 없다. # 백트래킹의 효과가 없다.
cnt = 0
cnt2 = 0
bit = [0] * N
f(0, N, K, 0)
print(cnt2) # 재귀함수의 호출 횟수