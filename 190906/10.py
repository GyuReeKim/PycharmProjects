# 격자판의 숫자 이어 붙이기
# 못풀었음

import pprint


def num(i, j):
    global word
    global result
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    word += arr[i][j]
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if ni >= 0 and ni < 4 and nj >= 0 and nj < 4:
            if len(word) != 7:
                print(k, word)
                num(ni, nj)
            else:
                print(k, word)
                result.append(word)

T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    pprint.pprint(arr, indent=4, width=40)
    word = ''
    result = []
    num(0, 0)
    print(result)