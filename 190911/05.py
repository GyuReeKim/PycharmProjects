# 7일차 - 미로1
# 풀다 말았음
import pprint


def find(i, j):
    return 1


T = 1
for tc in range(1, T+1):
    t = int(input())
    maze = [list(input()) for _ in range(16)]
    pprint.pprint(maze, indent=4, width=160)

    startI = 0
    startJ = 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                startI = i
                startJ = j
    print(startI, startJ)