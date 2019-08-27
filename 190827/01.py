grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())
for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))

    result = []
    k_result = ''
    for n in range(N):
        m, f, r = list(map(int, input().split()))
        all = m * 0.35 + f * 0.45 + r * 0.2
        result.append(all)
        if n == K-1:
            k_result = all
    sort_result = sorted(result, reverse=True)
    # print(sort_result)

    for i in range(N):
        if sort_result[i] == k_result:
            print(f'#{tc} {grade[i//(N//10)]}')