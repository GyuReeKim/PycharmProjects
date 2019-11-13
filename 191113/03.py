# [모의 SW 역량테스트] 홈 방범 서비스

# 서비스 영역의 크기 K
# 운영 비용 K*K + (K-1)*(K-1)

import sys
sys.stdin = open('03.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # M: 하나의 집이 지불가능한 비용
    city = [list(map(int, input().split())) for _ in range(N)]
    # print(city)

    house = []
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                house.append([i, j])
    # print(house)
    maxC = 0
    # [i, j] : 서비스 제공 지점
    for i in range(N):
        for j in range(N):
            # 서비스 지점과 집 사이의 거리
            distance = [0]*len(house)
            maxD = 0
            for d in range(len(house)):
                distance[d] = 1 + abs(i-house[d][0]) + abs(j-house[d][1])
                if distance[d] > maxD:
                    maxD = distance[d]
            # print(distance)

            # k 크기에 따른 이익 구하기
            # k의 최대 크기는 서비스 가능한 최대 크기
            for k in range(1, maxD+1):
                service_cost = k*k + (k-1)*(k-1)
                # print(service_cost)
                # 서비스 반경 안의 집의 수 count
                cnt = 0
                for l in range(len(distance)):
                    if distance[l] <= k:
                        cnt += 1
                # print(cnt)
                # 서비스 회사의 이익
                benefit = cnt * M - service_cost
                # print(benefit)
                # 손해를 보지 않고 서비스가 가능한 최대 집
                # 이익이 0일 수 있다.
                if benefit >= 0:
                    # print(cnt, benefit)
                    if cnt > maxC:
                        maxC = cnt
    print('#{} {}'.format(tc, maxC))