# 퍼펙트 셔플

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = input().split()

    left = []
    right = []
    for i in range(N):
        if N % 2:
            if i <= N//2:
                left.append(card[i])
            else:
                right.append(card[i])
        else:
            if i < N//2:
                left.append(card[i])
            else:
                right.append(card[i])

    result = []
    for i in range(N//2):
        result.append(left[i])
        result.append(right[i])

    if len(left) != len(right):
        result.append(left[-1])

    print('#{} {}'.format(tc, ' '.join(result)))