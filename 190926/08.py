# [파이썬 S/W 문제해결 구현] 2일차 - 전자카트


def perm():


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    