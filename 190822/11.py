# import pprint
T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    rcount = 0
    for i in range(N):
        for j in range(1, N):
            if puzzle[i][j] == 1:
                if puzzle[i][j-1] != 0:
                    puzzle[i][j] = puzzle[i][j-1] + 1
            if j == N-1 or puzzle[i][j+1] == 0:
                if puzzle[i][j] == K:
                    rcount += 1
    # print(rcount)
    # pprint.pprint(puzzle, indent=4, width=100)

    for i in range(N):
        for j in range(N):
            if puzzle[i][j] != 0:
                puzzle[i][j] = 1

    ccount = 0
    for i in range(1, N):
        for j in range(N):
            if puzzle[i][j] == 1:
                if puzzle[i-1][j] != 0:
                    puzzle[i][j] = puzzle[i-1][j] + 1
            if i == N-1 or puzzle[i+1][j] == 0:
                if puzzle[i][j] == K:
                    ccount += 1
    # print(ccount)
    # pprint.pprint(puzzle, indent=4, width=100)
    print('#{} {}'.format(tc, rcount + ccount))
