# 자기 방으로 돌아가기
import pprint


def idx(number):
    if number % 2:
        for i in range(200):
            if room[0][i] == number:
                return i

    else:
        for i in range(200):
            if room[2][i] == number:
                return i


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    room = [[0]*200 for _ in range(3)]
    for i in range(3):
        for j in range(200):
            if i == 0:
                room[i][j] = (j+1)*2-1
            elif i == 2:
                room[i][j] = (j+1)*2
    # pprint.pprint(room, indent=4, width=2000)
    for n in range(N):
        A, B = list(map(int, input().split()))

        idx1 = idx(A)
        idx2 = idx(B)
        # print(room)
        # for i in range(3):
        #     for j in range(200):
        #         if room[i][j] == A:
        #             idx1 = j
        #         if room[i][j] == B:
        #             idx2 = j

        print(idx1, idx2)
        for i in range(200):
            if idx1 <= idx2:
                if idx1 <= i <= idx2:
                    room[1][i] += 1
            else:
                if idx2 <= i <= idx1:
                    room[1][i] += 1

        maxV = 0
        for i in range(200):
            if room[1][i] > maxV:
                maxV = room[1][i]
        print(room[1])
    # print(room[1])
    # pprint.pprint(room, indent=4, width=2000)
    print('#{} {}'.format(tc, maxV))

# input
# 1
# 10
# 1 399
# 4 188
# 190 6
# 2 3
# 287 290
# 39 40
# 20 26
# 100 140
# 291 102
# 7 199