# 원재의 메모리 복구하기

T = int(input())
for tc in range(1, T+1):
    bit = list(input())
    base = ['0']*len(bit)
    cnt = 0
    for i in range(len(bit)):
        if base[i] != bit[i]:
            for j in range(i, len(bit)):
                base[j] = bit[i]
            cnt += 1
        if base == bit:
            break
    print('#{} {}'.format(tc, cnt))