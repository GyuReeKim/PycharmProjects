# 통역사 성경이
# 풀이중

# ord('A') = 65
# ord('Z') = 90
# ord('a') = 97
# ord('z') = 122

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    name_list = ['']*N
    while cnt != N:
        sentence = input()
        for i in range(len(sentence)):
            if sentence[i] == '.' or sentence[i] == '?' or sentence[i] == '!':
                cnt += 1
        words = sentence.split()
        print(words)

        sentence_cnt = 0
        name_cnt = 0
        for word in words:
            is_name = 1
            if word[-1] == '.' or word[-1] == '?' or word[-1] == '!':
                if 65 <= ord(word[0]) <= 90:
                    for i in range(1, len(word)-1):
                        if ord(word[i]) < 97 or ord(word[i]) > 122:
                            is_name = 0
                else:
                    is_name = 0
                if is_name == 1:
                    name_cnt += 1
                name_list[sentence_cnt] = str(name_cnt)
                word_cnt = 0
                sentence_cnt += 1
            else:
                if 65 <= ord(word[0]) <= 90:
                    for i in range(1, len(word)):
                        if ord(word[i]) < 97 or ord(word[i]) > 122:
                            is_name = 0
                else:
                    is_name = 0
                if is_name == 1:
                    name_cnt += 1
            print(word, name_cnt, sentence_cnt)
    print(name_list)