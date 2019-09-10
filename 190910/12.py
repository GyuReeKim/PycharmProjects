# 100만 이하의 모든 소수
# 제한시간 초과

for i in range(2, 1000001):
# for i in range(2, 11):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
        if cnt > 2:
            break
    else:
        print(i, end=' ')