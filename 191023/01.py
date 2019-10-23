# [S/W 문제해결 기본] 3일차 - 회문2

import sys
sys.stdin=open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    t = int(input())
    table = [list(input()) for _ in range(100)]
    # print(table)