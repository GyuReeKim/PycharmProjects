# Magnetic
# import pprint


def down(i, j):
    global table
    global N
    if table[i][j] == '3':
        return 1
    else:
        table[i][j] = '1'
        ni = i + 1
        nj = j
        if ni >= 1 and ni < N+2:
            if table[ni][nj] != '1' and table[ni][nj] != '2':
                if down(ni, nj) == 1:
                    return 1
        return 0


T = 10
for tc in range(1, T+1):
    N = int(input())
    table = [['3']*N]
    table += [input().split() for _ in range(N)]
    table += [['3']*N]
    # print(table)

    idx_1 = []
    idx_2 = []
    for i in range(N+2):
        for j in range(N):
            if table[i][j] == '1':
                idx_1.append([i, j])
            elif table[i][j] == '2':
                idx_2.append([i, j])
    # print(idx_1)
    # print(idx_2)

    for k in range(len(idx_1)):
        down(idx_1[k][0], idx_1[k][-1])

    # pprint.pprint(table, indent=4, width=70)

    cnt = 0
    for l in range(len(idx_2)):
        if table[idx_2[l][0]-1][idx_2[l][-1]] == '1':
            cnt += 1
    print('#{} {}'.format(tc, cnt))