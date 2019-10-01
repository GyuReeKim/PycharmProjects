# [S/W 문제해결 기본] 9일차 - 중위순회


def inorder(n):
    global word
    if n > 0:
        inorder(ch1[n])
        word += par[n]
        inorder(ch2[n])


T = 10
for tc in range(1, T+1):
    N = int(input())
    par = [0]*(N+1)
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)
    for i in range(N):
        node = input().split()
        if len(node) == 4:
            par[int(node[0])] = node[1]
            ch1[int(node[0])] = int(node[2])
            ch2[int(node[0])] = int(node[3])
        elif len(node) == 3:
            par[int(node[0])] = node[1]
            ch1[int(node[0])] = int(node[2])
        else:
            par[int(node[0])] = node[1]

    word = ''
    inorder(1)
    print('#{} {}'.format(tc, word))