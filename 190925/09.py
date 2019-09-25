# 배열 변형 문제 (input 2일차 sum 참고)

T = 10
for tc in range(1, T+1):
    t = int(input())
    num = [i+1 for i in range(30)]
    result = [0 for i in range(30)]
    arr = [list(map(int, input().split())) for _ in range(100)]
    # print(arr)

    for k in range(30):
        for i in range(100):
            for j in range(100):
                result[k] += abs(arr[i][j] - num[k])
    # print(result)

    minV = 10000000
    minI = 0
    for i in range(30):
        if result[i] < minV:
            minV = result[i]
            minI = i + 1
    print('#{} {} {}'.format(tc, minV, minI))