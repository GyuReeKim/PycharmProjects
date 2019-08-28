def f(N, card):
    for i in range(2, N):
        if card[i-2] > card[i-1]:
            if card[i-1] < card[i]:
                return -1
        elif card[i-2] < card[i-1]:
            if card[i-1] > card[i]:
                return -1
    return 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = [0] + list(map(int, input().split()))
    # L = card[1: N//2+1]
    # R = card[N//2+1:N+1]
    # print(L)
    # print(R)

    if f(N, card) == -1:
        print('#{} -1'.format(tc))
    else:
        print('#{} 1'.format(tc))