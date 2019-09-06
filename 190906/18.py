# 1일차 - 단순 2진 암호코드

rule = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    password = ''
    for i in range(N):
        P = input()
        for p in range(M-1, -1, -1):
            if P[p] == '1':
                password = P[p-56+1: p+1]
                break
    # print(password)

    num_list = []
    for i in range(8):
        for k in range(len(rule)):
            if password[i*7: (i+1)*7] == rule[k]:
                num_list.append(k)
    # print(num_list)

    add = 0
    num = 0
    for i in range(8):
        if i == 7:
            add += num_list[i]
            num += num_list[i]
        elif i % 2:
            add += num_list[i]
            num += num_list[i]
        else:
            add += num_list[i]
            num += num_list[i]*3
    # print(add, num)

    if num % 10:
        add = 0
    print('#{} {}'.format(tc, add))