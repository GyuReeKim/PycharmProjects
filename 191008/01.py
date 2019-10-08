# 최장 공통 부분 수열
# 제한시간 초과

T = int(input())
for tc in range(1, T+1):
    first, second = input().split()

    result = []
    for i in range(1, 1<<len(first)):
        res = ''
        for j in range(len(first)):
            if i & (1<<j):
                res += first[j]
        result.append(res)
    # print(result)

    maxV = 0
    for i in range(1, 1<<len(second)):
        res = ''
        for j in range(len(second)):
            if i & (1<<j):
                res += second[j]
        if res in result:
            if len(res) > maxV:
                maxV = len(res)
    print('#{} {}'.format(tc, maxV))