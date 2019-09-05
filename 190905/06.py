# 모음이 보이지 않는 사람

vowel = 'aeiou'
T = int(input())
for tc in range(1, T+1):
    word = input()

    # new_word = ''
    # for w in word:
    #     if w not in vowel:
    #         new_word += w
    # print('#{} {}'.format(tc, new_word))

    new_word = [w for w in word if w not in vowel]
    print('#{} {}'.format(tc, ''.join(new_word)))