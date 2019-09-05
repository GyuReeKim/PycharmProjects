# Magnetic
# 문제 발생


def down(i, j):
    global copy_table
    global N
    if copy_table[i][j] == '3':
        return 1
    else:
        copy_table[i][j] = '1'
        ni = i + 1
        nj = j
        if ni >= 0 and ni < N+2:
            if copy_table[ni][nj] != '1':
                if down(ni, nj) == 1:
                    return 1
        return 0


def up(i, j):
    global copy_table
    global N
    if copy_table[i][j] == '3':
        return 1
    else:
        copy_table[i][j] = '2'
        ni = i - 1
        nj = j
        if ni >= 0 and ni < N+2:
            if copy_table[ni][nj] != '2':
                if up(ni, nj) == 1:
                    return 1
        return 0


T = 1
for tc in range(1, T+1):
    N = int(input())
    table = [input().split() for _ in range(N)]
    print(table)
    copy_table = [['3']*N] + table + [['3']*N]
    print(table)
    print(copy_table)

    cnt = 0
    for i in range(1, N+1):
        for j in range(N):
            if table[i-1][j] == '1':
                if down(i, j) == 0:
                    cnt += 1
            # elif table[i-1][j] == '2':
            #     if up(i, j) == 1:
            #         cnt += 1
    print(table)
    print(copy_table)
    print('#{} {}'.format(tc, cnt))