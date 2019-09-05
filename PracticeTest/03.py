import sys
sys.stdin = open('모의1_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    maxR = price[N-1]
    maxGain = -1000
    for i in range(N-2, -1, -1):
        if(maxGain<maxR-price[i]):
            maxGain = maxR-price[i]
        if(maxR<price[i]):
            maxR = price[i]
    print('#{} {}'.format(tc, maxGain))