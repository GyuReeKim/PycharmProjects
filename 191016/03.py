# 성공적인 공연 기획

T = int(input())
for tc in range(1, T+1):
    real_clap = input()

    clap = 0
    fake_clap = 0
    for i in range(len(real_clap)):
        if clap >= i:
            clap += int(real_clap[i])
        else:
            clap += 1
            fake_clap += 1
            clap += int(real_clap[i])
    print('#{} {}'.format(tc, fake_clap))