# 정곤이의 단조 증가하는 수
# 제한시간 초과

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    mul_list = [str(A[i]*A[j]) for i in range(N-1) for j in range(i+1, N)]
    # mul_list = []
    # for i in range(N-1):
    #     for j in range(i+1, N):
    #         mul_list.append(str(A[i]*A[j]))
    # print(mul_list)

    # print(mul_list)

    maxV = -1
    for i in range(len(mul_list)):
        if mul_list[i] == ''.join(sorted(mul_list[i])):
            if maxV < int(mul_list[i]):
                maxV = int(mul_list[i])

    print('#{} {}'.format(tc, maxV))
