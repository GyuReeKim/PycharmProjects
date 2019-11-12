# 백준 17836번 공주님을 구해라!

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def bfs(i, j):
    global if_gram
    q = ['']*N*M
    visited = [[0 for b in range(M)] for a in range(N)]
    start = -1
    end = -1

    visited[i][j] = 1
    end += 1
    q[end] = [i, j]

    while start != end:
        start += 1
        i = q[start][0]
        j = q[start][1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < N and nj >= 0 and nj < M and visited[ni][nj] == 0:
                if maze[ni][nj] != '1':
                    visited[ni][nj] = visited[i][j] + 1
                    if ni == gram[0] and nj == gram[1]:
                        # print(visited)
                        if_gram = visited[ni][nj] - 1 + gram_to_princess
                    elif ni == N-1 and nj == M-1:
                        # print(visited)
                        return visited[ni][nj] - 1
                    end += 1
                    q[end] = [ni, nj]
    # print(visited)
    return -1


N, M, T = map(int, input().split())
maze = [list(input().split()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if maze[i][j] == '2':
            gram = [i, j]

gram_to_princess = (N-1) - gram[0] + (M-1) - gram[1]
# print([N-1, M-1], [gram[0], gram[1]])
# print(gram_to_princess)

if_gram = 0
result = bfs(0, 0)
# print(if_gram)

# 칼이 있을때
if if_gram != 0:
    # 도착을 못했을 때
    if result == -1:
        if if_gram <= T:
            print(if_gram)
        else:
            print('Fail')
    # 도착했을때
    else:
        # 칼을 뽑은 것의 시간이 짧은 경우
        if if_gram < result:
            # 정해진 시간안에 도착한 경우
            if if_gram <= T:
                print(if_gram)
            else:
                print('Fail')
        # 칼을 뽑지 않은 것의 시간이 짧은 경우
        else:
            # 정해진 시간안에 도착한 경우
            if result <= T:
                print(result)
            else:
                print('Fail')
# 칼이 없을 때
else:
    if result == -1:
        print('Fail')
    else:
        if result <= T:
            print(result)
        else:
            print('Fail')