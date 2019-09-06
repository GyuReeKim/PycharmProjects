# 다솔이의 다이아몬드 장식

"""
..#...#...#...#...#..
.#.#.#.#.#.#.#.#.#.#.
#.A.#.B.#.C.#.D.#.E.#
.#.#.#.#.#.#.#.#.#.#.
..#...#...#...#...#..
"""

T = int(input())
for tc in range(1, T+1):
    chars = input()
    arr = [['#'] if _ == 2 else ['.'] for _ in range(5)]

    for i in range(5):
        for j in range(len(chars)):
            if i == 0 or i == 4:
                arr[i].append('.#..')
            elif i == 1 or i == 3:
                arr[i].append('#.#.')
            else:
                arr[i].append('.{}.#'.format(chars[j]))
    # print(arr)

    for i in range(5):
        print(''.join(arr[i]))