# 전기버스2
# 백트래킹 사용해보기


def f(n, k, e, c): # n:정류장, k:종점, e:남은 에너지, c:교환횟수
    # global cnt
    global minV
    # cnt += 1
    if e < 0:
        return
    elif c > minV:
        return
    elif bat[0] - n <= bat[n]:
        if c+1 < minV:
            minV = c+1
            return
    elif n == k: # 종점에 도착하면
        if c < minV:
            minV = c
            return
    else:
        f(n+1, k, e-1, c) # 통과
        f(n+1, k, bat[n]-1, c+1) # 교체


T = int(input())
for tc in range(1, T+1):
    bat = list(map(int, input().split()))
    # cnt = 0
    minV = 100
    f(2, bat[0]-1, bat[1]-1, 0)
    print('#{} {}'.format(tc, minV))
    # print(cnt)