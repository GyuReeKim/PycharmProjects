T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*21 for _ in range(21)]
    for n in range(N):
        x, y, m, e = list(map(int, input().split()))

        for i in range(21):
            for j in range(21):
                if i == x+10 and j == y+10:
                    arr[i][j] += e
    print(arr)

