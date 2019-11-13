# 게리맨더링
# 아래의 코드를 사용하자

N = 3
M = 1<<3
for i in range(1, M//2):
    groupA = []
    groupB = []
    for j in range(N): # N: 비트 수
        # i를 비트로 검사한다.
        if i & (1<<j) != 0: # i의 j번 비트가 1이면
            groupA.append(j+1)
        else:
            groupB.append(j+1)
    print(groupA)
    print(groupB)
    print()