# 기지국
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 기지국과 집 정보 입력
    arr = [list(input()) for _ in range(N)]
    # arr = [input() for _ in range(N)] # 원하는 결과가 아님
    # print(arr)
    # 기지국 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A' or arr[i][j] == 'B' or arr[i][j] == 'C':
        # 커버되는 집 지우기
                if arr[i-1][j-1] == 'H':
                    arr[i-1][j-1] = 'X'
                if arr[i-1][j] == 'H':
                    arr[i-1][j] = 'X'
                if arr[i-1][j+1] == 'H':
                    arr[i-1][j+1] = 'X'
                if arr[i][j-1] == 'H':
                    arr[i][j-1] = 'X'
                if arr[i][j+1] == 'H':
                    arr[i][j+1] = 'X'
                if arr[i+1][j-1] == 'H':
                    arr[i+1][j-1] = 'X'
                if arr[i+1][j] == 'H':
                    arr[i+1][j] = 'X'
                if arr[i+1][j+1] == 'H':
                    arr[i+1][j+1] = 'X'
    print(arr)
    # 남은 집 개수 세기
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                count += 1
    print(count)