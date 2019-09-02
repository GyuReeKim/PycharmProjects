# 암호

T = int(input())
for tc in range(1, T+1):
    N, M, K = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    idx = M
    for k in range(1, K+1):

        while idx > len(numbers):
            idx -= len(numbers)

        left = numbers[:idx]
        right = numbers[idx:]

        if len(left) == 0:
            middle = right[-1] + right[0]
        elif len(right) == 0:
            middle = left[-1] + left[0]
        else:
            middle = left[-1] + right[0]

        numbers = left + [middle] + right
        idx += M

        result = [str(numbers[i]) for i in range(len(numbers)-1, -1, -1) if i >= len(numbers)-10]

    print('#{} {}'.format(tc, ' '.join(result)))







