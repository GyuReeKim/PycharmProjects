# [모의 SW 역량테스트] 숫자 만들기
# 순열 (비효율적)

import sys
sys.stdin = open('01.txt', 'r')


def perm(n, k):
    if n == k:
        # print(calc)
        calculation(calc)
    else:
        for i in range(n, k):
            calc[n], calc[i] = calc[i], calc[n]
            perm(n+1, k)
            calc[n], calc[i] = calc[i], calc[n]


def calculation(calc):
    global maxV, minV, num
    result = num[0]
    new_num = num[1:]
    # print(new_num)
    for i in range(N-1):
        if calc[i] == '+':
            result += new_num[i]
        elif calc[i] == '-':
            result -= new_num[i]
        elif calc[i] == '*':
            result *= new_num[i]
        else:
            result /= new_num[i]
            result = int(result)
    # print(result, calc)
    if result > maxV:
        maxV = result
    if result < minV:
        minV = result


temp_calc = ['+', '-', '*', '/']

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # num의 길이
    temp = list(map(int, input().split()))
    num = list(map(int, input().split()))
    calc = [temp_calc[k] for k in range(4) for t in range(temp[k])]
    # print(calc)
    maxV = -100000000
    minV = 100000000
    perm(0, N-1)
    print('#{} {}'.format(tc, maxV - minV))