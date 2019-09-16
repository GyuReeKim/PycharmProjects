# 정식이의 은행업무

T = int(input())
for tc in range(1, T+1):
    bi = input()
    tri = input()

    bi_result = []
    for i in range(len(bi)):
        left = bi[:i]
        right = bi[i+1:]
        if bi[i] == '0':
            middle = '1'
        else:
            middle = '0'
        new_bi = left + middle + right
        bi_result.append(int(new_bi, 2))
    # print(bi_result)

    tri_result = []
    for i in range(len(tri)):
        left = tri[:i]
        right = tri[i+1:]
        if tri[i] == '0':
            tri_result.append(int(left+'1'+right, 3))
            tri_result.append(int(left+'2'+right, 3))
        elif tri[i] == '1':
            tri_result.append(int(left+'0'+right, 3))
            tri_result.append(int(left+'2'+right, 3))
        else:
            tri_result.append(int(left+'0'+right, 3))
            tri_result.append(int(left+'1'+right, 3))
    # print(tri_result)

    for i in range(len(bi_result)):
        for j in range(len(tri_result)):
            if bi_result[i] == tri_result[j]:
                print('#{} {}'.format(tc, bi_result[i]))
                break