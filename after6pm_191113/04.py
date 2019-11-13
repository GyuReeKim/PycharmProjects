# 연구소
# 벽세우기

import sys
sys.stdin = open('04.txt', 'r')


def f(i, j, lab):
    pass


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
print(lab)

f(0, 0, lab)