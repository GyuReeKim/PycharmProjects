# [모의 SW 역량테스트] 점심 식사시간


def check(i, t):
    # 만들어보기


def f(k, pcnt):
    t0 = [0]*200 # 시간별로 계단에 머무는 사람 수 기록
    t1 = [0]*200
    for i in range(pcnt): # i번 사람이 어느 계단으로 갈지 결정
        if k & (1<<i) == 0: # 0번 계단으로 가는 경우
            check(i, 0)
        else: # 1번 계단으로 가는 경우
            check(i, 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stairs = []
    for i in range(N):
        for j in range(N):
                if room[i][j] == 1:
                    people.append([i, j])
                elif room[i][j] != 0:
                    stairs.append([i, j, room[i][j]])
    print(people)
    print(stairs)
    dis = [[0]*2 for i in range(len(people))]
    for i in range(len(people)):
        dis[i][0] = abs(people[i][0] - stairs[0][0]) + abs(people[i][1] - stairs[0][1]) # 사람i -> 계단0
        dis[i][1] = abs(people[i][0] - stairs[1][0]) + abs(people[i][1] - stairs[1][1]) # 사람i -> 계단0
    minT = 100000000
    for k in range(1<<len(people)): # 사람이 간 식당을 비트로 표시
        r = f(k, len(people))
        if r < minT:
            minT = r
    print('#{} {}'.format(tc, minT))