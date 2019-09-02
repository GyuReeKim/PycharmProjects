# 숫자 추가

T = int(input())
for tc in range(1, T+1):
    N, M, L = list(map(int, input().split()))
    num_list = list(map(int, input().split()))

    # result = []
    for i in range(M):
        idx, num = list(map(int, input().split()))

        left = num_list[:idx]
        right = num_list[idx:]

        num_list = []
        num_list.extend(left)
        num_list.extend([num])
        num_list.extend(right)
    # print(num_list)

    for i in range(len(num_list)):
        if i == L:
            print('#{} {}'.format(tc, num_list[i]))