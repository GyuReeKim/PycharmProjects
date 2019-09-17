# Baby-gin


def perm(n, k):
    global babygin
    if n == k: # n은 깊이, 바꿔줘야하는 고정 위치 # k는 바꿔줄 위치
        print(p)
        run = 0
        triplet = 0
        for a in range(2):
            s = p[3*a]
            r = 0
            t = 0
            for b in range(1, 3):
                if p[3*a+b] == s:
                    t += 1
                if int(p[3*a+b]) - int(p[3*a+(b-1)]) == 1:
                    r += 1
            if r == 2:
                run += 1
            if t == 2:
                triplet += 1
        if run + triplet == 2:
            babygin = 1
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            perm(n+1, k)
            p[n], p[i] = p[i], p[n]


p = list(input())
babygin = 0
perm(0, 6)
if babygin == 1:
    print('Babygin')
else:
    print('No')