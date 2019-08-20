# 반복문자 지우기

T = int(input())
for tc in range(1, T+1):
    txt = input()
    s = list()
    s.append(txt[0])
    for i in range(1, len(txt)):
        # 스택이 비어있거나, 스택의 맨 위 글자와 다르면 push(txt[i], 같으면 pop()
        if len(s) != 0 and s[-1] != txt[i]:
            s.append(txt[i])
        else:
            s.pop()
    print('#{} {}'.format(tc, len(s)))