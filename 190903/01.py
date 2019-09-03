# 의석이의 세로로 말해요

T = int(input())
for tc in range(1, T+1):
    chars = [list(input()) for _ in range(5)]

    maxL = 0
    for i in range(5):
        if len(chars[i]) > maxL:
            maxL = len(chars[i])

    for i in range(5):
        if len(chars[i]) < maxL:
            chars[i] += ['-']*(maxL-len(chars[i]))

    zip_chars = list(map(list, zip(*chars)))

    word = ''
    for i in range(maxL):
        for j in range(5):
            if zip_chars[i][j] != '-':
                word += zip_chars[i][j]
    print('#{} {}'.format(tc, word))

    # word = word.replace('-', '')
    # print(word)