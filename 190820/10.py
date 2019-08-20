# 초심자의 회문검사

T = int(input())
for tc in range(1, T+1):
    word = input()
    word_new = ''
    for w in word:
        if w != ' ':
            word_new += w
    # print(word_new)
    if word_new == word_new[::-1]:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))