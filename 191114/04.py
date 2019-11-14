# [모의 SW 역량테스트] 벽돌 깨기

import sys
sys.stdin = open('test.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    block = [list(map(int, input().split())) for _ in range(H)]
    print(block)

