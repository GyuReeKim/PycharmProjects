arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# print(len(arr))
# print(len(arr[0]))

# 가로의 합
for i in range(len(arr)):
    s = 0
    for j in range(len(arr[i])):
        s = s + arr[i][j]
    print(s)

# 세로의 합
for i in range(len(arr[0])): # 칸 변경
    s = 0
    for j in range(len(arr)): # 칸 고정, 줄 변경
        s = s + arr[j][i]
    print(s)

N = 4 # row 줄 수
M = 3 # column 칸 수

# 가로의 합
for i in range(N):
    s = 0
    for j in range(M):
        s = s + arr[i][j]
    print(s)

# 세로의 합
for i in range(M): # 칸 변경
    s = 0
    for j in range(N): # 칸 고정, 줄 변경
        s = s + arr[j][i]
    print(s)