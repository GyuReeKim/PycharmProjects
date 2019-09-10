# 9일차 - 사칙연산


def order(n):
    global parent
    # global calculator
    global calc
    if n > 0:
        order(ch1[n])
        order(ch2[n])
        if parent[n] == '+':
            result = calc.pop(-2) + calc.pop(-1)
            calc.append(result)
            # print(parent[n], calc)
        elif parent[n] == '-':
            result = calc.pop(-2) - calc.pop(-1)
            calc.append(result)
            # print(parent[n], calc)
        elif parent[n] == '*':
            result = calc.pop(-2) * calc.pop(-1)
            calc.append(result)
            # print(parent[n], calc)
        elif parent[n] == '/':
            result = calc.pop(-2) / calc.pop(-1)
            calc.append(result)
            # print(parent[n], calc)
        else:
            calc.append(int(parent[n]))
            # print(calc)


# calculator = ['+', '-', '*', '/']
T = 10
for tc in range(1, T+1):
    N = int(input())

    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)
    parent = [0]*(N+1)

    for n in range(N):
        node = input().split()
        print(node)
        for i in range(N+1):
            if i == int(node[0]):
                parent[i] = node[1]
                if len(node) == 3:
                    ch1[i] = int(node[2])
                elif len(node) == 4:
                    ch1[i] = int(node[2])
                    ch2[i] = int(node[3])
    # print(ch1)
    # print(ch2)
    # print(parent)

    calc = []
    order(1)
    print('#{} {}'.format(tc, int(calc[0])))

    # result = calc[0]
    # for i in range(1, N//2+1):
    #     if calc[i] == '+':
    #         calc.pop(i)
    #         result += calc[i]
    #     elif calc[i] == '-':
    #         calc.pop(i)
    #         result -= calc[i]
    #     elif calc[i] == '*':
    #         calc.pop(i)
    #         result *= calc[i]
    #     elif calc[i] == '/':
    #         calc.pop(i)
    #         result /= calc[i]
    # print('#{} {}'.format(tc, result))