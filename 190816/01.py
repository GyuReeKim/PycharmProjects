# s = input()
# print(s)
# # s = input().split()
# # print(s)
# # s = list(input())
# # print(s)
#
# s = s[::-1]
# print(s)

# 앞뒤 글자 바꾸기
s = list(input()) # 'ABCD' -> 'A', 'B', 'C', 'D'
# 'A' <-> 'D', 'B' <-> 'C'. 총 교환 횟수는 글자수//2
for i in range(0, len(s)//2): # 4//2 -> 2회, 인덱스 0, 1
    s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i] # list는 swap 가능
print(''.join(s))

# join 없이 출력하는 방법
for i in range(0, len(s)):
    print(s[i], end='')