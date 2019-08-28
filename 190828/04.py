# 원재의 메모리 복구하기

def f(bit, base_bit):
    count = 0
    for i in range(len(bit)):
        if bit[i] != base_bit[i]:
            count += 1
            for j in range(i, len(bit)):
                base_bit[j] = (base_bit[j] + 1) % 2
            if base_bit == bit:
                return count


T = int(input())
for tc in range(1, T+1):
    bit = list(map(int, input()))
    base_bit = [0]*len(bit)
    result = f(bit, base_bit)
    print('#{} {}'.format(tc, result))
