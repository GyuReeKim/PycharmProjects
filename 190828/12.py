# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
#
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
# 다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )
#
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

# 3
# 10 3
# 1 2 3 4 5 6 7 8 9 10
# 10 5
# 6262 6004 1801 7660 7919 1280 525 9798 5134 1821
# 20 19
# 3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394

#1 21
#2 11088
#3 1090

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))

    result = []
    for i in range(N-M+1):
        add = 0
        for j in range(i, i+M):
            add += A[j]
        result.append(add)
    print(result)

    maxV = 0
    minV = 1000000
    for i in range(len(result)):
        if result[i] > maxV:
            maxV = result[i]
        if result[i] < minV:
            minV = result[i]
    print('#{} {}'.format(tc, maxV-minV))

