# 원리 알아두기
def atoi(s): # '123' -> 123. '1' -> 1 -> 100의 자리, '2' -> 2 -> 10의 자리, '3' -> 3 -> 1의 자리
    n = 0
    for i in range(0, len(s)):
        n = n * 10
        # n = n + int(s[i])
        n = n + ord(s[i]) - ord('0')
    return n

s = input() # '123'
# print(len(s))
r = atoi(s)
print(r)