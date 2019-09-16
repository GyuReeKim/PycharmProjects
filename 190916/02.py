# 이진수

binary = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']

T = int(input())
for tc in range(1, T+1):
    N, number = input().split()
    result = ''
    for i in range(int(N)):
        if '0' <= number[i] <= '9':
            digit = ord(number[i]) - ord('0')
        else:
            digit = ord(number[i]) - ord('A') + 10
        for j in range(16):
            if digit == j:
                result += binary[j]
    print('#{} {}'.format(tc, result))