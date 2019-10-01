# 영준이의 카드 카운팅


def f(N):
    if len(N) == len(set(N)):
        return len(N)
    else:
        return -1


T = int(input())
for tc in range(1, T+1):
    card = list(input())
    S = []
    D = []
    H = []
    C = []
    for i in range(len(card)//3):
        if card[i*3] == 'S':
            S.append(card[i*3+1]+card[i*3+2])
        elif card[i*3] == 'D':
            D.append(card[i*3+1]+card[i*3+2])
        elif card[i*3] == 'H':
            H.append(card[i*3+1]+card[i*3+2])
        elif card[i*3] == 'C':
            C.append(card[i*3+1]+card[i*3+2])
    result = []
    if f(S) == -1 or f(D) == -1 or f(H) == -1 or f(C) == -1:
        print('#{} ERROR'.format(tc))
    else:
        result.append(str(13-f(S)))
        result.append(str(13-f(D)))
        result.append(str(13-f(H)))
        result.append(str(13-f(C)))
        print('#{} {}'.format(tc, ' '.join(result)))
