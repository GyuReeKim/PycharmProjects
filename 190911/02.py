# 영준이의 카드 카운팅


def overlap(l):
    if len(l) == len(set(l)):
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    card = input()

    s = []
    d = []
    h = []
    c = []
    for i in range(len(card)//3):
        if card[i*3] == 'S':
            s.append(card[i*3:(i+1)*3])
        elif card[i*3] == 'D':
            d.append(card[i*3:(i+1)*3])
        elif card[i*3] == 'H':
            h.append(card[i*3:(i+1)*3])
        elif card[i*3] == 'C':
            c.append(card[i*3:(i+1)*3])


    if overlap(s) == 0 or overlap(d) == 0 or overlap(h) == 0 or overlap(c) == 0:
        print('#{} ERROR'.format(tc))
    else:
        print('#{} {} {} {} {}'.format(tc, 13-len(s), 13-len(d), 13-len(h), 13-len(c)))