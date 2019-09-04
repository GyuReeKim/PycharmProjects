# 회문2
# import sys
# sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(100)]

    maxL = 0
    # maxL_word = ''
    for i in range(100):
        for j in range(100):
            word_r = ''
            for r in range(i,100):
                word_r += arr[r][j]
            print(word_r)
            #     if word_r == word_r[::-1]:
            #         if len(word_r) > maxL:
            #             maxL = len(word_r)
            #             # maxL_word = word_r
            # word_c = ''
            # for c in range(j, 100):
            #     word_c += arr[i][c]
            #     if word_c == word_c[::-1]:
            #         if len(word_c) > maxL:
            #             maxL = len(word_c)
            #             # maxL_word = word_c

    print('#{} {}'.format(N, maxL))
    # print(maxL_word)