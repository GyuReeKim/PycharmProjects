# 암호생성기

T = 10
for tc in range(1, T+1):
    t = int(input())
    numbers = input().split()

    n = 1
    while numbers[-1] > '0':
        if n > 5:
            n -= 5
        front = int(numbers.pop(0)) - n
        if front <= 0:
            front = 0
        numbers.append(str(front))
        n += 1

    print('#{} {}'.format(tc, ' '.join(numbers)))