# 암호
# 오류 발생

T = int(input())
for tc in range(1, T+1):
    N, M, K = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    for i in range(1, K+1):
        for n in range(len(numbers)):
            if i*K < len(numbers):
                if n == i*K:
                    left = numbers[:n]
                    right = numbers[n:]
            else:
                if i*K == len(numbers):
                    left = numbers
                    right = []
                elif n == i*K - len(numbers):
                    left = numbers[:n]
                    right = numbers[n:]

        numbers = []
        numbers.extend(left)
        if len(left) == 0:
            numbers.append(right[-1]+right[0])
        elif len(right) == 0:
            numbers.append(left[-1]+left[0])
        else:
            numbers.append(left[-1]+right[0])
        numbers.extend(right)
        print(numbers)

    print(numbers)