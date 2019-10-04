# 정곤이의 단조 증가하는 수

def increase(a):
    if len(a) == 1:
        return -1
    else:
        for k in range(len(a)-1):
            if int(a[k]) > int(a[k+1]):
                return -1
        return int(a)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    maxV = -1
    for i in range(N):
        for j in range(i+1, N):
            a = str(A[i]*A[j])
            if increase(a) > maxV:
                maxV = increase(a)
    print('#{} {}'.format(tc, maxV))