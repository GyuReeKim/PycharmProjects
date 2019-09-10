# 9일차 - 중위순회


def inorder(n):
    global parent
    global word
    if n > 0:
        inorder(ch1[n])
        word += parent[n]
        inorder(ch2[n])


T = 10
for tc in range(1, T+1):
    N = int(input())

    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    parent = [0] * (N+1)

    for n in range(N):
        node = input().split()
        # print(node)

        for i in range(N+1):
            if i == int(node[0]):
                parent[i] = node[1]
                if len(node) == 3:
                    ch1[i] = int(node[2])
                elif len(node) == 4:
                    ch1[i] = int(node[2])
                    ch2[i] = int(node[3])
    print(ch1)
    print(ch2)
    print(parent)
    word = ''
    inorder(1)
    print('#{} {}'.format(tc, word))