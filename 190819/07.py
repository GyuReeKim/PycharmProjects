# 반복문자 지우기

def repeat(txt):
    s = list()
    for i in range(len(txt)):
        s.append(txt[i])
        if len(s) > 1:
            if s[-1] == s[-2]:
                s.pop()
                s.pop()
    return len(s)

T = int(input())
for tc in range(1, T+1):
    words = input()
    print('#{} {}'.format(tc, repeat(words)))
