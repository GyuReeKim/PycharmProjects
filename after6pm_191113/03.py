# 캐슬 디펜스

import sys
sys.stdin = open('03.txt', 'r')


def defence(i, j, k, N, M, D):
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    print(visited)


N, M, D = map(int, input().split())
enemy = [list(map(int, input().split())) for _ in range(N)]
# print(enemy)

for i in range(M-2): # 왼쪽 궁수
    for j in range(i+1, M-1): # 가운데 궁수
        for k in range(j+1, M): # 오른쪽 궁수
            defence(i, j, k, N, M, D)