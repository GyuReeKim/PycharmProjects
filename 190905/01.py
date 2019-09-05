# 숫자 배열 회전

def rotation(arr):
    rotate_arr = list(map(list, zip(*arr)))
    for i in range(N):
        rotate_arr[i] = rotate_arr[i][::-1]
    return rotate_arr


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    arr_90 = rotation(arr)
    arr_180 = rotation(arr_90)
    arr_270 = rotation(arr_180)

    print('#{}'.format(tc))
    for i in range(N):
        print(''.join(arr_90[i]), ''.join(arr_180[i]), ''.join(arr_270[i]))