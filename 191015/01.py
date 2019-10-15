# 항구에 들어오는 배


def f(i):
    global visited
    global ship
    for k in range(i+1, N):
        for s in range(len(ship)):
            if happy[k] % ship[s] == 0:
                visited[k] = 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    happy = [int(input())-1 for _ in range(N)]
    visited = [0 for _ in range(N)]

    ship = []
    cnt = 0
    for i in range(1, N):
        if visited[i] == 0:
            ship.append(happy[i])
            visited[i] = 1
            cnt += 1
            f(i)
    print('#{} {}'.format(tc, cnt))
