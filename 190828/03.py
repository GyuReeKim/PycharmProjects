# 전기버스

T = int(input())
for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    stop = list(map(int, input().split()))

    bus_stop = []
    for i in range(N+1):
        if i == 0 or i == N or i in stop:
            bus_stop.append(1)
        else:
            bus_stop.append(0)
    # print(bus_stop)

    index_list = [N]
    for i in range(N, 0, -1):
        if i == index_list[-1]:
            index = -1
            for k in range(1, K+1):
                if bus_stop[i-k] == 1:
                    index = i-k
                    if i-k == 0:
                        break
            index_list.append(index)
    # print(index_list)

    if -1 in index_list:
        result = 0
    else:
        result = len(index_list)-2
    print('#{} {}'.format(tc, result))


