# [S/W 문제해결 기본] 10일차 - 비밀번호

import sys
sys.stdin=open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    length, num = input().split()
    password = list(num)
    # print(password)
    stop = 0
    while stop == 0:
        for i in range(int(length)-1):
            if password[i] == '-':
                stop = 1
                break
            elif password[i] == password[i+1]:
                password.pop(i)
                password.pop(i)
                password.append('-')
                password.append('-')
                break
    result = ''.join(password).replace('-', '')
    print('#{} {}'.format(tc, result))