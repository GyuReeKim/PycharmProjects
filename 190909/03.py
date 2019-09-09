# 현주의 상자 바꾸기

T = int(input())
for tc in range(1, T + 1):
    N, Q = list(map(int, input().split()))
    box = ['0'] * N
    for q in range(1, Q + 1):
        L, R = list(map(int, input().split()))
        for i in range(L, R + 1):
            box[i - 1] = str(q)
    print('#{} {}'.format(tc, ' '.join(box)))

# 힌트

# for tc in range(int(input())):
#     N, Q = map(int, input().split())
#     change = [list(map(int, input().split())) for _ in range(Q)]
#     ori = [0] * N