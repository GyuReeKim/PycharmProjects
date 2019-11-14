# [모의 SW 역량테스트] 요리사

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    # print(S)

    s = [_ for _ in range(N)]

    minV = 1000000
    for i in range(1<<N):
        a = []
        b = []
        for j in range(N):
            if i & (1<<j):
                a.append(s[j])
            else:
                b.append(s[j])
        if len(a) == len(b):
            A = 0
            B = 0
            for r in range(len(a)):
                for c in range(len(a)):
                    if r != c:
                        A += S[a[r]][a[c]]
                        B += S[b[r]][b[c]]
            diff = abs(A-B)
            if diff < minV:
                minV = diff
    print('#{} {}'.format(tc, minV))