# 파스칼의 삼각형

def pa(n):
    result = ['1']
    for i in range(1, n):
        if i == 1:
            result = ['1', '1']
        else:
            add = []
            for r in range(1, len(result)):
                add.append(str(int(result[r-1]) + int(result[r])))
            # print(add)
            for a in range(len(add)):
                result.pop()
            result += add
            result.append('1')
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pascal = [[] for p in range(N)]
    # print(pascal)

    print('#{}'.format(tc))
    for n in range(N):
        print(' '.join(pa(n+1)))
    # print(pascal)




