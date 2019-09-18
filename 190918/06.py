# 병합정렬


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
        # print(left, right)
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
        # print(left, right)
        # print(result)
        if len(left) != 0 and len(right) != 0 and left[-1] > right[-1]:
            cnt += 1
    return result


L = [2, 2, 1, 1, 3]
cnt = 0
print(merge_sort(L))


# def merge(left, right):
#     global cnt
#     i = 0
#     j = 0
#     result = []
#     while (i < len(left)) & (j < len(right)):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#
#     return result