# [알고리즘 월말평가 문제3] : 미네랄 모으기
# 백트래킹 추가

# 1 60
# 2 100
# 3 220
# 4 0
# 5 150
# 6 904

import sys
sys.stdin = open('input.txt', 'r')


def f(n, k, s, e, r): # s: 미네랄의 합계, d: 이동거리 합계, r: 전체 합
    global maxV
    if e >= 0:
        # print(s)
        if maxV < s:
            maxV = s
    else:
        return
    if n == k:
        return
    elif s + r < maxV:
        return
    else:
        f(n+1, k, s + mineral[n][2], e-2*dis[n], r-mineral[n][2])
        f(n+1, k, s, e, r-mineral[n][2])


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    robot = [0, 0] # 로봇의 좌표
    mineral = [] # 미네랄 정보
    dis = [] # 미네랄까지의 거리
    maxV = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                robot[0], robot[1] = i, j # 로봇의 위치 기록
            elif arr[i][j] > 1:
                mineral.append([i, j, arr[i][j]]) # 미네랄의 좌표, 양 기록
    # print(mineral)
    for m in mineral:
        dis.append(abs(robot[0]-m[0]) + abs(robot[1]-m[1])) # 각 미네랄까지의 거리
    s = 0
    for i in range(len(mineral)):
        s += mineral[i][2]
    f(0, len(mineral), 0, C, s)
    print('#{} {}'.format(tc, maxV))
