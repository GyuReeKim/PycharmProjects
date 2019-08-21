T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    count = 0
    save = 0
    while count != M:
        save = A.pop(0)
        A.append(save)
        count += 1
    print('#{} {}'.format(tc, A[0]))