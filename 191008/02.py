# 세상의 모든 팰린드롬 2

T = int(input())
for tc in range(1, T+1):
    word = input()

    result = 1
    for i in range(len(word)//2):
        if word[i] == '*' or word[len(word)-1-i] == '*':
            break
        elif word[i] != word[len(word)-1-i]:
            result = 0
            break
    if result == 1:
        print('#{} Exist'.format(tc))
    else:
        print('#{} Not exist'.format(tc))