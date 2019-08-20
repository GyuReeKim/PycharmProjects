# 봉우리

# N = 7
N = 10
# A = [1, 2, 1, 2, 1, 2, 1]
A = [7, 2, 3, 4, 1, 2, 5, 4, 5, 6]

# result = [2]
# count = 0
# for i in range(1, N):
#     if A[i] - A[i-1] > 0:
#         result.append(1)
#     else:
#         if result[-1] == 1:
#             count += 1
#         result.append(0)
# print(count)

# slope = 0
# cnt = 0
# for i in range(1, N):
#     if A[i-1] > A[i]:
#         if slope == 1: # 내리막이고 이전까지 오르막이면
#             cnt += 1 # 오르막 -> 내리막인 봉우리이므로
#             slope = 0
#     else:
#         slope = 1
# print(cnt)

# 골짜기

# result = [2]
# count = 0
# for i in range(1, N):
#     if A[i] - A[i-1] < 0:
#         result.append(0)
#     else:
#         if result[-1] == 0:
#             count += 1
#         result.append(1)
# print(count)

# slope = 2
# cnt = 0
# for i in range(1, N):
#     if A[i-1] < A[i]:
#         if slope == 0:
#             cnt += 1
#             slope = 1
#     else:
#         slope = 0
# print(cnt)