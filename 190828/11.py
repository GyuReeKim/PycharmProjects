T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))
    for i in range(N-1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
    # print(numbers)

    count = [0]*(numbers[-1]+1)
    # print(count)

    for i in range(len(count)):
        for j in range(N):
            if numbers[j] == i:
                count[i] += 1
    # print(count)

    max_count = 0
    max_index = 0
    for i in range(len(count)):
        if count[i] >= max_count:
            max_count = count[i]
            max_index = i
    print('#{} {} {}'.format(tc, max_index, max_count))