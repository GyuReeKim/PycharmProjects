# Professional 건초더미

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    hay = [int(input()) for _ in range(N)]
    mid = sum(hay)//N
    cnt = 0
    for i in range(N):
        cnt += abs(mid - hay[i])
    print('#{} {}'.format(tc, cnt//2))