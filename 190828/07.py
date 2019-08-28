# 정곤이의 단조 증가하는 수
# 제한시간 초과

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    maxV = -1
    num = 0
    for i in range(N-1):
        for j in range(i+1, N):
            num = str(A[i]*A[j])
            num_list = list(num)
            if num_list == sorted(num_list):
                if int(num) > maxV:
                    maxV = int(num)

    print('#{} {}'.format(tc, maxV))
