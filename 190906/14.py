# 10일차 - 비밀번호


def delete(P):
    cnt = 0
    for i in range(int(len(P))-1):
        if P[i] != '-' and P[i] == P[i+1]:
            cnt += 1
            P.pop(i)
            P.pop(i)
            P.append('-')
            P.append('-')
    if cnt != 0:
        delete(P)


T = 10
for tc in range(1, T+1):
    N, password = input().split()
    P = [password[_] for _ in range(int(N))]
    delete(P)
    nP = ''
    for i in range(int(N)):
        nP += P[i]
    new_password = nP.replace('-', '')
    print('#{} {}'.format(tc, new_password))