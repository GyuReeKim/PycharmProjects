# 암호 스캔 코드
# 선생님 코드

def f(N, M, s):
    used = [[0]*M for _ in range(N)] # 확인된 암호패턴 영역을 표시
    total = 0
    for i in range(N):
        j = M*4-1 # 비트 패턴의 끝을 탐색
        while j > 0:
            if s[i][j] == '1' and used[i][j] == 0: # 패턴이 시작되면
                pwd = [0]*8
                col = j
                for k in range(7, -1, -1):
                    cnt = [0, 0, 0] # 1, 0, 1의 각 개수 저장
                    while s[i][col] == '0': # 1이 나올 때까지 0인 구간 스킵
                        col -= 1
                    while s[i][col] == '1': # 1이 나오면 1인 구간의 길이 확인
                        cnt[0] += 1
                        col -= 1
                    while s[i][col] == '0': # 0인 구간의 길이
                        col[1] += 1
                        col -= 1
                    while s[i][col] == '1': # 1인 구간의 길이
                        cnt[2] += 1
                        col -= 1
                    ratio = min(cnt)
                    cnt[0] //= ratio
                    cnt[1] //= ratio
                    cnt[2] //= ratio
                    idx = cnt[0]*100 + cnt[1]*10 + cnt[2]
                    pwd[k] = pat.index(idx)
                check = (pwd[0]+pwd[2]+pwd[4]+pwd[6])*3+pwd[1]+pwd[3]+pwd[5]+pwd[7]
                if check % 10 == 0:
                    total += sum(pwd)

                row = i
                while s[row][j] == '1':
                    for k in range(col, j+1):
                        used[row][k] = 1
                    row += 1
                j = col
            else:
                j -= 1
    return total


b = ['0000', '0001', '0010', '0011',
     '0100', '0101', '0110', '0111',
     '1000', '1001', '1010', '1011',
     '1100', '1101', '1110', '1111']

pat = [112, 122, 221, 114, 231, 132, 411, 213, 312, 211]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = [input() for _ in range(N)]
    s = ['']*N

    for i in range(N): # N개의 16진수 라인
        for j in range(M):
            s[i] += b[int(a[i][j], 16)] # 2진수의 문자열 형태로 저장
    print('#{} {}'.format(tc, f(N, M, s)))