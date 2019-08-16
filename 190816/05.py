# 문자열 비교
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)

    count = 0
    for s in range(0, M-N+1):
        if str2[s:s+N] == str1:
            count = 1
    print('#{} {}'.format(tc, count))

# T = int(input())
#
# for tc in range(1, T+1):
#     str1 = input()
#     str2 = input()
#
#     for i in range(len(str2)):
#         if str1 == str2[i:i+len(str1)]:
#             result = 1
#             break
#         else:
#             result = 0
#
#     print("#{} {}".format(tc, result))



