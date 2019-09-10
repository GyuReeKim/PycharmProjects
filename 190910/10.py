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

    result = []
    for i in range(N):
        add = ''
        for j in range(i, N):
            add += num[j]
            result.append(int(add))
    final = sorted(list(set(result)))

    for k in range(100):
        if k not in final:
            print('#{} {}'.format(tc, k))
            break