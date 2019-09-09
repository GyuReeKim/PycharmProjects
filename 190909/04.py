# Professional 건초더미

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    hay = [int(input()) for _ in range(N)]
    max_hay = max(hay)
    min_hay = min(hay)
    cnt = 0
    if max_hay == min_hay:
        print('#{} {}'.format(tc, cnt))
    else:
        while max(hay) != min(hay):
            max_hay = max(hay)
            min_hay = min(hay)
            for i in range(N):
                if hay[i] == max_hay:
                    hay[i] -= 1
                    break
            for i in range(N):
                if hay[i] == min_hay:
                    hay[i] += 1
                    break
            cnt += 1
        print('#{} {}'.format(tc, cnt))
