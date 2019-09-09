# 늘어지는 소리 만들기

T = int(input())
for tc in range(1, T+1):
    word = list(input())
    H = int(input())
    hyphen = list(map(int, input().split()))
    # print(word)

    for h in range(H):
        for i in range(len(word)):
            if i == 0 and hyphen[h] == 0:
                word[0] = '-' + word[0]
            elif hyphen[h]-1 == i:
                word[i] += '-'
    print('#{} {}'.format(tc, ''.join(word)))
