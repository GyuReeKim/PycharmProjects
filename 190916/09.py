# 암호코드 스캔
# 푸는중..

code = ['3211', '2221', '2122', '1411', '1132', '1231', '1114', '1312', '1213', '3112']
binary = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [input() for _ in range(N)]
    # pprint.pprint(arr, indent=4, width=M*10)

    res = []
    for i in range(N):
        J = M
        temp = ''
        temp_list = []
        for j in range(M-1, -1, -1):
            if j < J and arr[i][j] != '0':
                temp = arr[i][j-14+1: j+1] + temp
                J = j-14
                # print(temp, J)
            elif j == J and arr[i][j] == '0':
                if temp not in temp_list and len(temp) != 0:
                    temp_list.append('0'+temp)
                temp = ''
            elif j == J and arr[i][j] != '0':
                temp = arr[i][j-14+1: j+1] + temp
                J = j-14
                # print(temp, J)
        if temp not in temp_list and len(temp) != 0:
            temp_list.append('0'+temp)
        res.extend(temp_list)
    res = list(set(res))
    print(res)

    ###################################################
    # res = []
    # for i in range(N):
    #     temp_list = []
    #     temp = ''
    #     J = 0
    #     for j in range(M - 1, -1, -1):
    #         if len(temp_list) == 0:
    #             if arr[i][j] != '0':
    #                 temp = arr[i][j - 15 + 1:j + 1]
    #                 J = j - 15 + 1
    #         else:
    #             if j == J and arr[i][j] != '0':
    #                 temp += arr[i][j - 15 + 1:j + 1]
    #                 J = j - 15 + 1
    #                 # if len(temp) == 15:
    #                 #     temp_list.append(temp)
    #                 # temp = ''
    #     print(temp)
    #     # print(temp_list)
    #     res.extend(temp_list)
    # res = list(set(res))
    # print(res)
    ###################################################

    final = 0
    for i in range(len(res)):
        bi_code = ''
        for j in range(len(res[i])):
            if '0' <= res[i][j] <= '9':
                digit = ord(res[i][j]) - ord('0')
            else:
                digit = ord(res[i][j]) - ord('A') + 10
            for k in range(16):
                if digit == k:
                    bi_code += binary[k]
        print(len(bi_code), bi_code)

        R = 0
        for r in range(1, len(res)+1):
            if 60*(r-1) <= len(bi_code) <= 60*r:
                R = r
                for b in range(len(bi_code)-1, -1, -1):
                    if bi_code[b] == '1':
                        bi_code = bi_code[b-(56*r)+1:b+1]
                        break
        print(R, len(bi_code), bi_code)



        cnt = 1
        cnt_str = ''
        for k in range(1, len(bi_code)):
            if k == len(bi_code)-1:
                if bi_code[k] != bi_code[k-1]:
                    cnt_str += str(cnt//R)
                    cnt_str += '1'
                else:
                    cnt += 1
                    cnt_str += str(cnt//R)
            elif bi_code[k] != bi_code[k-1]:
                cnt_str += str(cnt//R)
                cnt = 1
            else:
                cnt += 1
        print(cnt_str)

        result = []
        for k in range(8):
            # print(cnt_str[4*k:4*(k+1)])
            for c in range(len(code)):
                if cnt_str[4*k:4*(k+1)] == code[c]:
                    result.append(c)
                    break
        print(result)

        if len(result) == 8:
            is_right = 0
            for k in range(8):
                if k == 7:
                    is_right += result[k]
                elif k % 2:
                    is_right += result[k]
                else:
                    is_right += result[k]*3

            if is_right % 10 == 0:
                final += sum(result)
    print('#{} {}'.format(tc, final))