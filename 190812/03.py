# import sys
# sys.stdin = open('input.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):

numbers = list(map(int, input().split()))
max_num = numbers[0]
for number in numbers:
    if number > max_num:
        max_num = number
print(max_num)