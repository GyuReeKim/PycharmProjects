# 화섭이의 정수 나열
# Runtime error

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    if N//20 == 0:
        num = input().split()
    else:
        num = []
        for k in range(N//20):
            num2 = input().split()
            num.extend(num2)
    # print(num)

    for k in range(100):
        result = 0
        for i in range(N-1, -1, -1):
            add = ''
            for j in range(i, N):
                add += num[j]
                # print(add)
                if int(add) == k:
                    result = 1
        if result == 0:
            print('#{} {}'.format(tc, k))
            break