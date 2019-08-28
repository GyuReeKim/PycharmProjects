# IM 기출1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [0] + list(map(int, input().split()))
    base_room = [0]*(N+1)

    count = 0
    for i in range(1, N+1):
        if room[i] != base_room[i]:
            count += 1
            for j in range(i, N+1):
                if j % i == 0:
                    base_room[j] = (base_room[j] + 1) % 2

    print('#{} {}'.format(tc, count))