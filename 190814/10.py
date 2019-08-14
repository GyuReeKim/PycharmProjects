def bi_search(N, key):
    left = 1
    right = N
    count = 0
    while left <= right:
        center = (left + right) // 2
        if key == center:
            count += 1
            return count

        elif key > center:
            left = center

        elif key < center:
            right = center
        count += 1
    return -1


T = int(input())
for tc in range(1, T+1):
    p, pa, pb = list(map(int, input().split()))

    if bi_search(p, pa) < bi_search(p, pb):
        print('#{} A'.format(tc))
    elif bi_search(p, pa) > bi_search(p, pb):
        print('#{} B'.format(tc))
    else:
        print('#{} 0'.format(tc))
