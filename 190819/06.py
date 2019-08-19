# 괄호검사

def pl(txt):
    s = list()
    for i in range(len(txt)):
        if txt[i] == '{':
            s.append(txt[i])
        elif txt[i] == '(':
            s.append(txt[i])

        elif txt[i] == '}':
            if len(s) == 0 or s[-1] != '{':
                return 0
            else:
                s.pop()
            # if len(s) == 0:
            #     return 0
            # elif s[-1] == '{':
            #     s.pop()
            # else:
            #     return 0
        elif txt[i] == ')':
            if len(s) == 0 or s[-1] != '(':
                return 0
            else:
                s.pop()
            # if len(s) == 0:
            #     return 0
            # elif s[-1] == '(':
            #     s.pop()
            # else:
            #     return 0

    if len(s) != 0:
        return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    code = input()
    print('#{} {}'.format(tc, pl(code)))