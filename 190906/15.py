# 3일차 - String

T = 10
for tc in range(1, T+1):
    t = int(input())
    word = input()
    sentence = input()

    cnt = 0
    for i in range(len(sentence)-len(word)+1):
        if sentence[i:i+len(word)] == word:
            cnt += 1
    print('#{} {}'.format(tc, cnt))