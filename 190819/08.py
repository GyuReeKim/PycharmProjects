# 0816 회문2

# import pprint
#
# arr = [[0]*100 for a in range(100)]
#
# for i in range(100):
#     char = list(input())
#     for j in range(100):
#         arr[i][j] = char[j]
#
#
#
# row = []
# for i in range(100): # 열
#     for j in range(100): # 행
#         for k in range(100, 0, -1):
#             pal = arr[i][j:j+k]
#             if pal == pal[::-1]:
#                 row.append(pal)
# print(row)
#
#
# # pprint.pprint(arr, indent=4, width=1000)

####
import pprint

arr = [[] for a in range(100)]

for i in range(100):
    char = input()
    arr[i] = char

pprint.pprint(arr, indent=4, width=1000)

result = []
for i in range(100):
    for j in range(100):
        for k in range(100, 0, -1):
            row = arr[i][j: j+k+1]
            col = arr[j][i: i+k+1]
            if row == row[::-1]:
                result.append(row)
            if col == col[::-1]:
                result.append(row)
print(result)



# long = 0
# for r in result:
#     if len(r) > long:
#         long = len(r)
#
# print(long)