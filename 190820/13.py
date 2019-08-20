# Forth

T = int(input())
for tc in range(1, T+1):
    Forth = list(map(str, input().split()))
    # print(Forth)

    result = ''
    f_stack = []
    calc = 0
    for f in range(len(Forth)):
        if Forth[f] != '+' and Forth[f] != '-' and Forth[f] != '*' and Forth[f] != '/' and Forth[f] != '.':
            f_stack.append(int(Forth[f]))
        elif Forth[f] == '+':
            if len(f_stack) >= 2:
                calc = f_stack[-2] + f_stack[-1]
                f_stack.pop()
                f_stack.pop()
                f_stack.append(calc)
                calc = 0
            else:
                result = 'error' # 연산할 숫자가 없을 때
                break
        elif Forth[f] == '-':
            if len(f_stack) >= 2:
                calc = f_stack[-2] - f_stack[-1]
                f_stack.pop()
                f_stack.pop()
                f_stack.append(calc)
                calc = 0
            else:
                result = 'error'
                break
        elif Forth[f] == '*':
            if len(f_stack) >= 2:
                calc = f_stack[-2] * f_stack[-1]
                f_stack.pop()
                f_stack.pop()
                f_stack.append(calc)
                calc = 0
            else:
                result = 'error'
                break
        elif Forth[f] == '/':
            if len(f_stack) >= 2:
                calc = f_stack[-2] / f_stack[-1]
                f_stack.pop()
                f_stack.pop()
                f_stack.append(int(calc))
                calc = 0
            else:
                result = 'error'
                break
        elif Forth[f] == '.':
            result = f_stack[0]
    if len(f_stack) != 1: # f_stack에 숫자가 더 남아있으면 오류
        result = 'error'
    print('#{} {}'.format(tc, result))