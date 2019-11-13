# [모의 SW 역량테스트] 숫자 만들기
# 재귀함수 이용

import sys
sys.stdin = open('01.txt', 'r')


def f(n, k, s, c): # n: 사용할 숫자 idx, k: 사용할 숫자의 최대 idx, s: 계산 결과, c: 연산자 사용
    global maxV, minV
    if n == k:
        if s > maxV:
            maxV = s
        if s < minV:
            minV = s
    else:
        # +를 사용할 수 있는 경우
        if c[0] > 0:
            c[0] -= 1
            f(n+1, k, s+num[n], c)
            c[0] += 1
        # -를 사용할 수 있는 경우 (비교해야하기 때문에 if문을 사용해야 한다.)
        if c[1] > 0:
            c[1] -= 1
            f(n+1, k, s-num[n], c)
            c[1] += 1
        # *를 사용할 수 있는 경우
        if c[2] > 0:
            c[2] -= 1
            f(n+1, k, s*num[n], c)
            c[2] += 1
        # /를 사용할 수 있는 경우
        if c[3] > 0:
            c[3] -= 1
            f(n+1, k, int(s/num[n]), c)
            c[3] += 1



T = int(input())
for tc in range(1, T+1):
    N = int(input()) # num의 길이
    calc = list(map(int, input().split()))
    # print(calc)
    num = list(map(int, input().split()))
    result = num[0]
    num = num[1:]
    maxV = -100000000
    minV = 100000000
    f(0, N-1, result, calc)
    # print(maxV, minV)
    print('#{} {}'.format(tc, maxV - minV))