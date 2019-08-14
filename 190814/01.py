# View (조망권)

T = 10
for tc in range(T):
    N = int(input())
    h = list(map(int, input().split()))
    s = 0
    for i in range(2, N-2):
        if h[i] > h[i-1] and h[i] > h[i-2] and h[i] > h[i+1] and h[i] > h[i+2]:
            diff = h[i]-h[i-1]
            if diff > h[i]-h[i-2]:
                diff = h[i]-h[i-2]
            if diff > h[i]-h[i+1]:
                diff = h[i]-h[i+1]
            if diff > h[i]-h[i+2]:
                diff = h[i]-h[i+2]
            s = s + diff
    print('#{} {}'.format(tc+1, s))