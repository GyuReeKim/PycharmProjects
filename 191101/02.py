# 퍼펙트 셔플

import sys
sys.stdin=open('input2.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    origin = list(input().split())
    # print(origin)
    left = []
    right = []
    for i in range(N):
        if N % 2:
            if i <= N//2:
                left.append(origin[i])
            else:
                right.append(origin[i])
        else:
            if i < N//2:
                left.append(origin[i])
            else:
                right.append(origin[i])
    # print(left, right)

    result = []
    for i in range(len(right)):
        result.append(left[i])
        result.append(right[i])
    if N % 2:
        result.append(left[-1])
    print('#{} {}'.format(tc, ' '.join(result)))