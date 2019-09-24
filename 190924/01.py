# 테네스의 특별한 소수
# 시간초과

prime = []
for i in range(2, 1001):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
            if cnt > 2:
                cnt = 0
                break
    if cnt == 2:
        prime.append(i)
print(prime)

result = 0
T = int(input())
for tc in range(1, T+1):
    D, A, B = map(int, input().split())
    result = 0
    for i in range(len(prime)):
        if A <= i <= B:
            if str(D) in str(i):
                result += 1
        elif i > B:
            break
    print('#{} {}'.format(tc, result))