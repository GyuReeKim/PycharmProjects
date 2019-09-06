# 1일차 - 단순 2진 암호코드
# 런타임 에러

rule = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    password = [input() for _ in range(N)]
    # print(password)

    real = []
    for i in range(N):
        for j in range(M-1, -1, -1):
            if password[i][j] == '1':
                real.append(password[i][j-56+1:j+1])
                break
    # print(real)

    result = 0
    # for i in range(len(real)):
    num = []
    for j in range(8):
        for k in range(9):
            if real[0][j*7: (j+1)*7] == rule[k]:
                num.append(k)
    # print(num)

    add = 0
    for k in range(8):
        if k == 7:
            add += num[k]
        elif k % 2:
            add += num[k]
        else:
            add += num[k]*3

    # print(add)
    if add % 10 != 0:
        result = 0
    else:
        result += sum(num)
    print('#{} {}'.format(tc, result))

