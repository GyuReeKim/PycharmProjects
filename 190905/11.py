# 암호문3


def I(x, s):
    global password
    left = password[:int(x)]
    right = password[int(x):]
    password = left + s + right
    return password


def D(x, y):
    global password
    for k in range(int(y)):
        password.pop(int(x))
    return password


def A(s):
    global password
    password += s
    return password


T = 10
for tc in range(1, T+1):
    N = int(input())
    password = input().split()
    C = int(input())
    command = input().split()
    # print(password)
    # print(command)

    for i in range(C):
        if command[i] == 'I':
            x = command.pop(i+1)
            y = command.pop(i+1)
            s = []
            for k in range(int(y)):
                s.append(command.pop(i+1))
            password = I(x, s)
        elif command[i] == 'D':
            x = command.pop(i+1)
            y = command.pop(i+1)
            password = D(x, y)
        elif command[i] == 'A':
            y = command.pop(i+1)
            s = []
            for k in range(int(y)):
                s.append(command.pop(i+1))
            password = A(s)

    result = [password[i] for i in range(10)]
    print('#{} {}'.format(tc, ' '.join(result)))