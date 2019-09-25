# 백준 - 게리맨더링


def bfs(area, N):
    q = [area[0]] # 큐 생성, 시작점 인큐
    v = [0]*(N+1)
    v[area[0]] = 1 # 시작점 방문표시
    total = 0 # 선거구 인구
    while len(q) != 0:
        i = q.pop(0) # i 선거구 선택
        total += p[i] # i 선거구 인구 더함
        for j in area: # 같은 선거구 지역 j가
            if adj[i][j] == 1 and v[j] == 0: # j 선거구가 i에 인접이고, 아직 처리전이면
                q.append(j)
                v[j] = v[i] + 1
    for i in area:
        if v[i] == 0: # 연결되지 않은 선거구가 있으면
            return 0
    return total # 모든 선거구가 연결된 경우


# # append, pop 사용 안할경우
# def bfs(area, N):
#     f = -1
#     b = -1
#     q = [0]*N
#     v = [0]*(N+1)
#
#     b += 1
#     q[b] = area[0]
#     v[area[0]] = 1
#
#     total = 0
#     while f != b:
#         f += 1
#         i = q[f]
#         total += p[i]
#         for j in area:
#             if adj[i][j] == 1 and v[j] == 0:
#                 b += 1
#                 q[b] = j
#                 v[j] = v[i] + 1
#     for i in area:
#         if v[i] == 0:
#             return 0
#     return total


N = int(input())
p = [0] + list(map(int, input().split()))
adj = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1): # 인접행렬 생성
    node = list(map(int, input().split()))
    for j in node[1:]:
        adj[i][j] = 1
        adj[j][i] = 1 # 무향 그래프로 표시되므로
# print(adj)

minV = 1000000000000
for i in range(1, (1<<N)//2): # 비트 연산으로 두 그룹으로 나눔. 절반만 선택하면 나머지는 다른 그룹에 속함
    areaA = []
    areaB = []
    for j in range(N):
        if i & (1<<j) != 0:
            areaA.append(j+1) # j+1을 선거구 번호로 활용
        else:
            areaB.append(j+1)
    # print(areaA, areaB)
    # 각 그룹을 탐색하고 인구 차이를 구함
    rA = bfs(areaA, N) # 선거구가 끊어져 있는 경우 0 리턴
    rB = bfs(areaB, N) # 선거구가 이어진 경우 선거구 인구의 합 리턴

    if rA * rB != 0: # 양쪽 선거구가 정상적으로 연결되어 있으면
        if minV > abs(rA-rB):
            minV = abs(rA-rB)

# 모든 구역 분할에 대한 검토가 끝나면
if minV == 1000000000000:
    minV = -1

print(minV)