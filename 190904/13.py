# 이진 탐색

def cnt(p, P):
    l = 1
    r = p
    c = 0
    cnt = 0
    while c != P:
        cnt += 1
        c = int((l+r)/2)
        if P < c:
            r = c
        else:
            l = c
    return cnt

T = int(input())
for tc in range(1, T+1):
    p, Pa, Pb = list(map(int, input().split()))

    cntA = cnt(p, Pa)
    cntB = cnt(p, Pb)

    if cntA < cntB:
        print('#{} A'.format(tc))
    elif cntA > cntB:
        print('#{} B'.format(tc))
    else:
        print('#{} 0'.format(tc))
