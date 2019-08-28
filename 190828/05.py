# 정곤이의 단조 증가하는 수
# 제한시간 초과

def comparative(i, mul_list):
    for j in range(len(mul_list[i])-1):
        if int(mul_list[i][j]) > int(mul_list[i][j+1]):
            return 0
        else:
            return 1


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

    for i in range(len(mul_list)):
        result = comparative(i, mul_list)
        if result == 0:
            mul_list[i] = 0
    # print(mul_list)

    result = [int(mul_list[i]) for i in range(len(mul_list))]
    print('#{} {}'.format(tc, max(result)))
