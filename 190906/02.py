# 회문2
# import pprint

T = 10
for tc in range(1, T+1):
    t = int(input())
    arr = [list(input()) for _ in range(100)]
    # pprint.pprint(arr, indent=4, width=70)

    maxV = 0
    for i in range(100):
        for j in range(100):
            row = ''
            for r in range(j, 100):
                row += arr[r][i]
                if row == row[::-1]:
                    if len(row) > maxV:
                        maxV = len(row)
            col = ''
            for c in range(j, 100):
                col += arr[i][c]
                # print(chars)
                if col == col[::-1]:
                    if len(col) > maxV:
                        maxV = len(col)
    print('#{} {}'.format(tc, maxV))