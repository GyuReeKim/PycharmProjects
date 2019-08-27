# A형 문제 풀다가 말았음
import pprint
arr = [[0]*21 for _ in range(21)]
N = int(input())
for n in range(N):
    x, y, m, e = list(map(int, input().split()))

    for i in range(21):
        for j in range(21):
            if i == x+10 and j == y+10:
                arr[i][j] += e

pprint.pprint(arr, indent=4, width=210)