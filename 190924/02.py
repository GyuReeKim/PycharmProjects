# 7일차 - 최소 비용


def find(N):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    D = [[1000000000]*N for i in range(N)] # 각 칸 까지의 최소 연료 소비량
    D[0][0] = 0
    q = [] # 소비량이 갱신된 지역의 인접 지역 저장용
    q.append((0, 0))
    while q: # 더이상 갱신 되는 경우가 없을 때까지 만복
        t = q.pop(0)
        for i in range(4):
            r = t[0] + dr[i] # 이동할 인접 칸 좌표
            c = t[1] + dc[i]
            if r >= 0 and r < N and c >= 0 and c < N: # 유효한 범위면
                diff = 0
                ...