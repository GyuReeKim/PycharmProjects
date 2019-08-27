# 간단한 압축 풀기(0826)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    k_sum = 0
    chars = ''
    for n in range(N):
        C, K = input().split()
        k_sum += int(K)
        chars += C * int(K)
    # print(k_sum)
    # print(chars)

    char_list = []
    for i in range(k_sum//10):
        char = ''
        for j in range(10):
            char += chars[10*i+j]
            # print(char)
        char_list.append(char)

    char_last = chars[10*(k_sum//10):-1] + chars[-1]
    char_list.append(char_last)

    # print(char_list)
    print(f'#{tc}')
    for i in range(len(char_list)):
        print(char_list[i])
