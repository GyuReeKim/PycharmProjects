# 10일차 - 비밀번호

T = 1
for tc in range(1, T+1):
    N, num = input().split()
    number = [num[_] for _ in range(int(N))]
    result = 0
    for k in range(int(N)//2):
        for i in range(int(N)-1):
            if number[i] != '-' and number[i] == number[i+1]:
                result = 1
                number.pop(i)
                number.pop(i)
                number.append('-')
                number.append('-')
        if result == 0:
            break
    password = ''.join(number).replace('-', '')
    print('#{} {}'.format(tc, password))