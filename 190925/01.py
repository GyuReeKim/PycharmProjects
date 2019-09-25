# 최대 상금
def find(n, k, c):
    global maxV
    global minC
    if c == 0 or n == k:
        s = 0
        for i in range(k):
            s = s*10 + int(card[i])
        if maxV <= s:
            maxV = s
            if minC > c
                minC = c
    else:
        lst = list(str(card))
        for i in range(k):
            card[n], card[i] = card[i], card[n]
            cnt = 1 if n! = i else 0
            find(n+1, k, c-cnt)
            card[n], card[i] = card[i], card[n]


T = int(input())
for tc in range(1, T+1):
    ...