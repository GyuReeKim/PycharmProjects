T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = input()
    for i in range(0, N):
        print(num[i])
    card = [0] * 10
    for i in range(0, N):
        v = int(num[i])
        card[v] = card[v] + 1

    maxIdx = 0
    for i in range(0, 10):
        if(card[maxIdx]<=card[i]):
            maxIdx = i
    print('#{} {} {}'.format(tc, maxIdx, card[maxIdx]))