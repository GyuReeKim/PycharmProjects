# Baby-gin
# 선생님 코드 # 적다 말았음


def perm(n, k):
    global babygin
    if n == k: # n은 깊이, 바꿔줘야하는 고정 위치 # k는 바꿔줄 위치
        print(p)
        run = 0
        tri = 0
        if p[0] == p[1] == p[2]:
            tri += 1
        if p[3] == p[4] == p[5]:
            tri += 1
        if p[2] == p[1]+1 == p[0]+2:
            run += 1
        if p[5] == p[4]+1 == p[3]+2:
            run += 1
        if run + tri == 2:
            print('baby-gin')
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            perm(n+1, k)
            p[n], p[i] = p[i], p[n]


p = list(input())
perm(0, 6)

