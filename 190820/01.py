# 백만장자 프로젝트

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = list(map(int, input().split()))

    buy = 0
    max_price = S[-1]
    for n in range(N-1, -1, -1):
        if S[n] > max_price:
            max_price = S[n]
        else:
            buy = buy + max_price - S[n]

    print('#{} {}'.format(tc, buy))