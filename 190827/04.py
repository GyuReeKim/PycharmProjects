T = int(input())
for tc in range(1, T+1):
    TXY = input()

    T = ['S', 'D', 'H', 'C']

    card = [[0]*13 for _ in range(4)]
    # print(card)

    for i in range(4):
        for j in range(13):
            for c in range(len(TXY)-2):
                if TXY[c] == T[i]:
                    num = int(TXY[c+1] + TXY[c+2])
                    if j == num-1:
                        card[i][j] += 1
    # print(card)

    count_list = []
    for i in range(4):
        count = 0
        for j in range(13):
            if card[i][j] == 0:
                count += 1
            elif card[i][j] > 1:
                count_list.append('ERROR')
                break
        count_list.append(str(count))
    # print(count_list)
    if 'ERROR' in count_list:
        result = 'ERROR'
    else:
        result = ' '.join(count_list)

    print(f'#{tc} {result}')