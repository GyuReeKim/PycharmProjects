# 게리맨더링
# 부분집합
# 푸는중

import sys
sys.stdin = open('01.txt', 'r')

N = int(input())
population = list(map(int, input().split()))
info = [list(map(int, input().split())) for _ in range(N)]
print(info)