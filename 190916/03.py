# 이진수2
# [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

T = int(input())
for tc in range(1, T+1):
    N = input()
    # print(N)
    for i in range(1<<(len(N)-2)):
        add = 0
        res = []
        for j in range(len(N)-2):
            if i & (1<<j) != 0:
                add += 1/(2**(j+1))
                res.append('1')
            else:
                res.append('0')
        # print(res)
        if add == float(N):
            break
    else:
        add = -1
    if add == -1:
        print('#{} overflow'.format(tc))
    else:
        print('#{} {}'.format(tc, ''.join(res)))