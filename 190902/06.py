# 수열 편집

T = int(input())
for tc in range(1, T+1):
    N, M, L = list(map(int, input().split()))
    num_list = list(map(int, input().split()))

    for i in range(M):
        edit = input().split()
        if edit[0] == 'I':
            left = num_list[:int(edit[1])]
            right = num_list[int(edit[1]):]
            num_list = left + [int(edit[-1])] + right
            # print(num_list)

        elif edit[0] == 'D':
            left = num_list[:int(edit[-1])]
            right = num_list[int(edit[-1])+1:]
            num_list = left + right
            # print(num_list)
        else:
            left = num_list[:int(edit[1])]
            right = num_list[int(edit[1])+1:]
            num_list = left + [int(edit[-1])] + right
            # print(num_list)
    # print(num_list)

    if L >= len(num_list):
        result = -1
    else:
        result = num_list[L]
    print('#{} {}'.format(tc, result))
