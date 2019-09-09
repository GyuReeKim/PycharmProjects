# A형
# 1부터 5까지 두 그룹으로 나누기..
N = 5
# 2진수로 표시해보기...
for i in range(1, (1<<N)-1): # 그룹 A 속한 원소를 나타내는 2진수 i
    A = []
    B = []
    for j in range(N):
        if i & (1<<j) != 0: # i의 j번 비트가 1이면
            A.append(j+1)
        else:
            B.append(j+1)
    print(A, B)