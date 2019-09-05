# 준환이의 운동관리

T = int(input())
for tc in range(1, T+1):
    L, U, X = list(map(int, input().split()))

    if L < X < U:
        print('#{} 0'.format(tc))
    elif X > U:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc, L-X))