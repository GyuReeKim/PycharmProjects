# 개구리 뛰기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rock = [0] + list(map(int, input().split()))
    K = int(input())

    last = 0
    cnt = 0
    result = 1
    for i in range(1, N+1):
        if rock[i] - rock[i-1] > K:
            result = 0
            break
        else:
            if rock[i] - rock[last] > K:
                last = i-1
                cnt += 1
    if result == 0:
        print('Case #{}'.format(tc))
        print(-1)
    else:
        print('Case #{}'.format(tc))
        print(cnt+1)
