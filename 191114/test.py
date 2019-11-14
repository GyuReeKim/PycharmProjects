import sys
sys.stdin = open('test.txt', 'r')


def npr(n, k, W, H):
    global minV
    if n == k:
        print(p)
    else:
        for i in range(W): # 중복순열
            p[n] = i
            npr(n+1, k, W, H)
            if minV == 0:
                return


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    org = [list(map(int, input().split())) for _ in range(H)]
    p = [0]*N
    minV = 100000000
    npr(0, N, W, H)
    print('#{} {}'.format(tc, minV))