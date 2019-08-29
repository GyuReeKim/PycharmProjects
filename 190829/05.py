# 기차 사이의 파리

T = int(input())
for tc in range(1, T+1):
    D, A, B, F = list(map(int, input().split()))

    h = D / (A+B)

    print('#{} {:.10f}'.format(tc, F*h))