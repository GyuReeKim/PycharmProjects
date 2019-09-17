# 재귀 호출을 통한 순열 생성
# 정렬된 순서가 아님
# 주어진 3개의 숫자로 만드는 순열


def perm(n, k):
    if n == k: # n은 깊이, 바꿔줘야하는 고정 위치 # k는 바꿔줄 위치
        print(p)
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            perm(n+1, k)
            p[n], p[i] = p[i], p[n]


p = [1, 2, 3]
perm(0, 3)