# 암호코드 스캔
# 검증 필요함
# 실패
import pprint

code = ['3211', '2221', '2122', '1411', '1132', '1231', '1114', '1312', '1213', '3112']
binary = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [input() for _ in range(N)]
    # pprint.pprint(arr, indent=4, width=M*10)
    res = []
    for i in range(N):
        temp = ''
        for j in range(M):
            if arr[i][j] == '0' and arr[i][j-1] != '0':
                res.append(temp)
                temp = ''
            else:
                if arr[i][j] != '0':
                    temp += arr[i][j]
    res = list(set(res))
    print(res)

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
        # print(len(bi_code), bi_code)
        R = 0
        for r in range(1, len(res)+1):
            if 60*(r-1) <= len(bi_code) <= 60*r:
                R = r
                for b in range(len(bi_code)-1, -1, -1):
                    if bi_code[b] == '1':
                        bi_code = bi_code[b-(56*r)+1:b+1]
                        break
        # bi_code = '0000001111001100001111000011000011000011110011111111001100110000001111001111000000110011001111111100111111001111'
        # R = 2
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

        is_right = 0
        for k in range(8):
            if k == 7:
                is_right += result[k]
            elif k % 2:
                is_right += result[k]
            else:
                is_right += result[k]*3
        print(is_right)

        if is_right % 10 == 0:
            final += sum(result)
    print('#{} {}'.format(tc, final))
