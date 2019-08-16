# import pprint
# 회문인가?

# 길이가 5인 회문이 존재하는가?
# 길이가 4인 회문이 존재하는가
# 길이가 3인 회문이 존재하는가?

# palindrome

T = int(input())
for tc in range(1, T+1):

    N, M = list(map(int, input().split()))
    arr = [[0]*N for n in range(N)]

    for i in range(N):
        chars = input()
        for j in range(N):
            arr[i][j] = chars[j]

    # pprint.pprint(arr, indent=4, width=200)

    for i in range(N):
        row = ''
        col = ''
        for j in range(N):
            row += arr[i][j]
            col += arr[j][i]

        print(row)
        for r in range(N-M+1):
            pal_r = row[r: r+M]
            if pal_r == pal_r[::-1]:
                print('#{} {}'.format(tc, pal_r))
                break

        print(col)
        for c in range(N-M+1):
            pal_c = col[r: r+M]
            if pal_c == pal_c[::-1]:
                print('#{} {}'.format(tc, pal_c))
                break
