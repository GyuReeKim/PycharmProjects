# 캐슬 디펜스


def defence(aw1, aw2, aw3, N, M, D):
    target = [[0]*M for _ in range(N)]
    hit = 0
    for i in range(N):
        for j in range(M):
            target[i][j] = enemy[i][j]
    for i in range(N): # 사격 횟수
        # 궁수와 거리가 D 이내에서 가장 가까운 적 중 맨 왼쪽의 적을 맞춤
        shoot(aw1, target, N, M, D)
        shoot(aw2, target, N, M, D)
        shoot(aw3, target, N, M, D)
        for r in range(N): # 화살에 맞는 적을 가려냄
            for c in range(M):
                if target[r][c] > 1:
                    hit += 1
                    target[r][c] = 0
        for r in range(N-1, 0, -1):
            for c in range(M):
                target[r][c] = target[r-1][c] # 성벽쪽으로 이동
        for c in range(0, M):
            target[0][c] = 0 # 가장 외곽의 적은 성벽쪽으로 이동하고 없음
    return hit


def shoot(aw, target, N, M, D):
    q = []
    v = [[0]*M for _ in range(N)] # 이미 확인한 칸은 표시
    dr = [0, -1, 0]
    dc = [-1, 0, 1]
    q.append(N-1) # 궁수와 거리가 1인 칸은 바로 추가해준다.
    q.append(aw)
    v[N-1][aw] = 1
    while len(q) != 0:
        r = q.pop(0)
        c = q.pop(0)
        if target[r][c] > 0 and v[r][c] <= D:
            target[r][c] += 1
            return
        elif v[r][c] > D: # 적이 없어도 사거리가 D보다 크면 return
            return
        for k in range(3): # 왼쪽, 앞, 오른쪽
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if v[nr][nc] == 0: # 아직 확인안한 값
                    q.append(nr)
                    q.append(nc)
                    v[nr][nc] = v[r][c] + 1



N, M, D = map(int, input().split())
enemy = [list(map(int, input().split())) for _ in range(N)]
maxV = 0
for i in range(M-2): # 맨 왼쪽 궁수
    for j in range(i+1, M-1): # 가운데 궁수
        for k in range(j+1, M): # 오른쪽 궁수
            kill = defence(i, j, k, N, M, D)
            if maxV < kill:
                maxV = kill
print(maxV)