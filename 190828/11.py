# 0에서9까지숫자가적힌N장의카드가주어진다.
# 가장많은카드에적힌숫자와카드가몇장인지출력하는프로그램을만드시오.
# 카드장수가같을때는적힌숫자가큰쪽을출력한다.
#
# [입력]
# 첫줄에테스트케이스개수T가주어진다.(1 ≤ T ≤ 50 )
# 다음줄부터테스트케이스의첫줄에카드장수N이주어진다.(5 ≤ N ≤ 100 )
# 다음줄에N개의숫자ai가여백없이주어진다.(0으로시작할수도있다.)  (0 ≤ ai ≤ 9)
#
# [출력]
# 각줄마다"#T"(T는테스트케이스번호)를출력한뒤, 가장많은카드의숫자와장수를차례로출력한다.

# 3
# 5
# 49679
# 5
# 08271
# 10
# 7797946543

# 1 9 2
# 2 8 1
# 3 7 3

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))
    for i in range(N-1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
    # print(numbers)

    count = [0]*(numbers[-1]+1)
    # print(count)

    for i in range(len(count)):
        for j in range(N):
            if numbers[j] == i:
                count[i] += 1
    # print(count)

    max_count = 0
    max_index = 0
    for i in range(len(count)):
        if count[i] >= max_count:
            max_count = count[i]
            max_index = i
    print('#{} {} {}'.format(tc, max_index, max_count))