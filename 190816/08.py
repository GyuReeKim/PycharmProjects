# 다시풀어야함
import pprint

arr = [[0]*5 for ar in range(5)]
# A = [9, 20, 2, 18, 11, 19, 1, 25, 3, 21, 8, 24, 10, 17, 7, 15, 4, 16, 5 ,6, 12, 13, 22, 23, 14]
a = 0
for i in range(5):
    A = list(map(int, input().split()))
    for j in range(5):
        arr[i][j] = A[j]
        a += 1

pprint.pprint(arr, indent=4, width=50)
print()

num = 1
for i in range(5):
    for j in range(5):
        if i % 2 == 0:
            arr[i][j] = num
            num += 1
        else:
            arr[4-i][4-j] = num
            num += 1

pprint.pprint(arr, indent=4, width=50)


# 9 20 2 18 11
# 19 1 25 3 21
# 8 24 10 17 7
# 15 4 16 5 6
# 12 13 22 23 14