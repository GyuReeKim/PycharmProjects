# 화섭이의 정수 나열

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = ''
    while len(num) != N:
        num += ''.join(input().split())
    # print(num)

    cnt = 0
    while str(cnt) in num:
        cnt += 1
    print('#{} {}'.format(tc, cnt))