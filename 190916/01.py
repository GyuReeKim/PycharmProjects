# 직사각형과 점

T = int(input())
for tc in range(1, T+1):
    x1, y1, x2, y2 = list(map(int, input().split()))
    N = int(input())
    result = [0, 0, 0]
    for n in range(N):
        x, y = list(map(int, input().split()))

        if x == x1 or x == x2 or y == y1 or y == y2:
            result[1] += 1
        else:
            for i in range(x1+1, x2):
                for j in range(y1+1, y2):
                    if i == x and j == y:
                        result[0] += 1
                    else:
                        result[2] += 1
    result = [str(result[i]) for i in range(3)]
    print('#{} {}'.format(tc, ' '.join(result)))