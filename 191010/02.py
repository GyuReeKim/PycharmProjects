# 홀수 피라미드
# 푸는중


def f(n):
    global start, end, l
    cnt = 0
    while cnt != n:
        l = cnt*2 + 1
        start = end + 2
        end += start + (l-1)*2
        cnt += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    start = 0
    end = -1
    l = 0
    f(N)
    print(start, end)