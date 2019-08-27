# import pprint
# def main():
#     print('Hello World')
#
#
# if __name__ == "__main__":
#     main()

T = int(input())
for tc in range(1, T+1):
    N, M, K = list(map(int, input().split()))

    arr = [[0]*M for _ in range(N)]
    # print()
    # pprint.pprint(arr, indent=4, width=10*M)
    max_c = 0
    # status = ''
    for k in range(K):
        n1, m1, n2, m2, c = list(map(int, input().split()))
        if k == 0:
            for i in range(N):
                for j in range(M):
                    if n1 <= i <= n2 and m1 <= j <= m2:
                        if c > arr[i][j]:
                            arr[i][j] = c
                            if c > max_c:
                                max_c = c
        status = ''
        if k != 0:
            if max_c > c:
                for i in range(N):
                    for j in range(M):
                        if n1 <= i <= n2 and m1 <= j <= m2:
                            if arr[i][j] > c:
                                status = 'duplicated'
        if k != 0:
            if status != 'duplicated':
                for i in range(N):
                    for j in range(M):
                        if n1 <= i <= n2 and m1 <= j <= m2:
                            if c > arr[i][j]:
                                arr[i][j] = c
                                if c > max_c:
                                    max_c = c


        # pprint.pprint(arr, indent=4, width=10 * M)
        # print(max_c)

    # print('#{}'.format(tc))
    # pprint.pprint(arr, indent=4, width=10*M)

    colors = []
    for color in range(11):
        count = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == color:
                    count += 1
        colors.append(count)
    print('#{} {}'.format(tc, max(colors)))