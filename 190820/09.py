# 패턴 마디의 길이
T = int(input())
for tc in range(1, T+1):
    string = input()

    # result = []
    word = ''
    for s in range(len(string)):
        word = string[:s+1]
        # print(word)
        if word == string[s+1:2*(s+1)]:
            print('#{} {}'.format(tc, len(word)))
            break
    # print(result)