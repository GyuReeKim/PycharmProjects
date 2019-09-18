# 병합 정렬
# Gateway 오류


def merge_sort(L):
    if len(L) <= 1:
        return L
    middle = len(L)//2
    left = L[:middle]
    right = L[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    global cnt
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
        if len(left) != 0 and len(right) != 0 and left[-1] > right[-1]:
            cnt += 1
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    cnt = 0
    point = merge_sort(L)[N//2]
    print('#{} {} {}'.format(tc, point, cnt))