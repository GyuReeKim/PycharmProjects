# 달팽이
import pprint

c = 1
N = 3
k = N
direct = 1
arr = [[0]*N for _ in range(N)]

i = 0 # 시작 칸의 인덱스
j = -1 # 현재 위치로 부터 k번 이동 해야 하므로

while True:
    # 수평이동
    for h in range(k):
        j += direct
        arr[i][j] = c
        c += 1
    k -= 1 # 이동 거리 감소
    if k == 0: # 이동 거리가 0이면 중단
        break
    # 수직이동
    for v in range(k):
        i += direct
        arr[i][j] = c
        c += 1
    direct *= -1 # 수직->수평으로 바뀔때 인덱스 증감 바꾸기
pprint.pprint(arr, indent=4, width=N*10)