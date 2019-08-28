# 정곤이의 단조 증가하는 수

def up(num):
    number = str(num)
    if len(number) != 1:
        for i in range(1, len(number)):
            if number[i-1] > number[i]:
                return 0
        else:
            return 1
    else:
        return 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    maxV = -1
    num = 0
    for i in range(N-1):
        for j in range(i+1, N):
            num = A[i]*A[j]
            if up(num) == 1:
                if num > maxV:
                    maxV = num

    print('#{} {}'.format(tc, maxV))
