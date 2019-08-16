# 글자수

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    str1_dict = {}
    for s1 in str1:
        if s1 in str1_dict:
            str1_dict[s1] += 1
        else:
            str1_dict[s1] = 1
    # print(str1_dict)

    str2_dict = {}
    for key in str1_dict:
        for s2 in str2:
            if s2 == key:
                if s2 in str2_dict:
                    str2_dict[s2] += 1
                else:
                    str2_dict[s2] = 1
    # print(str2_dict)

    count = 0
    for key, val in str2_dict.items():
        if val > count:
            count = val
    print('#{} {}'.format(tc, count))