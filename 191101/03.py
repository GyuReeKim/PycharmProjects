# 부분 수열의 합

import sys
sys.stdin=open('input3.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = 0
    for i in range(1<<N):
        temp = 0
        for j in range(N):
            if i & (1<<j):
                temp += A[j]
        if temp == K:
            cnt += 1
    print('#{} {}'.format(tc, cnt))