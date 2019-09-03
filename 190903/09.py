T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    mul = []
    for i in range(N-1):
        for j in range(1, N):
            num = A[i]*A[j]
            mul.append(num)
    print(mul)