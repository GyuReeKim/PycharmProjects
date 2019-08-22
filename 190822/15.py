# 숫자 배열 회전
# 함수로 수정중

def change(N):
    arr_9 = []
    for i in range(N):
        row = ''
        for j in range(N):
            row += arr[N-1-j][i]
        # print(row)
        arr_9.append(row)
    # print(arr_9)
    new_arr.append(arr_9)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    # print(arr)

    new_arr = []
    arr_9 = []
    for i in range(N):
        row = ''
        for j in range(N):
            row += arr[N-1-j][i]
        # print(row)
        arr_9.append(row)
    # print(arr_9)
    new_arr.append(arr_9)

    arr_18 = []
    for i in range(N):
        row = ''
        for j in range(N):
            row += arr_9[N - 1 - j][i]
        # print(row)
        arr_18.append(row)
    # print(arr_18)
    new_arr.append(arr_18)

    arr_27 = []
    for i in range(N):
        row = ''
        for j in range(N):
            row += arr_18[N - 1 - j][i]
        # print(row)
        arr_27.append(row)
    # print(arr_27)
    new_arr.append(arr_27)

    # print(new_arr)

    print('#{}'.format(tc))
    for i in range(N):
        result = []
        for j in range(3):
            result.append(new_arr[j][i])
        print(' '.join(result))