# 장훈이의 높은 선반
# 승재오빠 코드

case = int(input())
for tc in range(case):
    N, B = map(int, input().split())
    tall = list(map(int, input().split()))

    res = []
    for i in range(1 << N):
        res2 = []
        for j in range(N):
            if i & (1 << j):
                res2.append(tall[j])
        res.append(sum(res2))

    sumlist = []
    for x in range(len(res)):
        if res[x] >= B:
            sumlist.append(res[x] - B)

    print("#{} {}".format(tc+1, min(sumlist)))



