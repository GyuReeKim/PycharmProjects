# 이진탐색


def inorder(n):
    global cnt
    global num1
    global num2
    if n > 0:
        inorder(ch1[n])
        cnt += 1
        if n == 1:
            num1 = cnt
        if n == N//2:
            num2 = cnt
        inorder(ch2[n])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    parent = [i for i in range(N+1)]
    ch1 = [2*i if 2*i <= N else 0 for i in range(N+1)]
    ch2 = [0 if i == 0 else 2*i+1 if 2*i+1 <= N else 0 for i in range(N+1)]

    # print(parent)
    # print(ch1)
    # print(ch2)
    cnt = 0
    num1 = 0
    num2 = 0
    inorder(1)
    print('#{} {} {}'.format(tc, num1, num2))