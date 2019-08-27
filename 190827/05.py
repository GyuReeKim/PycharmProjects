# 스위치 켜고 끄기
switch = int(input())
status = input().split()
students = int(input())
for student in range(students):
    gender, number = list(map(int, input().split()))

    if gender == 1:
        for i in range(1, switch+1):
            if i % number == 0:
                if status[i-1] == '1':
                    status[i-1] = '0'
                else:
                    status[i-1] = '1'
    elif gender == 2:
        for i in range(1, switch+1):
            if switch % 2 == 0:
                if i == number and number <= switch//2:
                    for j in range(number):
                        if j == 0:
                            if status[i-1] == '1':
                                status[i-1] = '0'
                            else:
                                status[i-1] = '1'
                        else:
                            if status[i-1-j] != status[i-1+j]:
                                break
                            else:
                                if status[i-1-j] == '1':
                                    status[i-1-j] = '0'
                                    status[i-1+j] = '0'
                                else:
                                    status[i-1-j] = '1'
                                    status[i-1+j] = '1'
                elif i == number and number > switch//2:
                    for j in range(switch - number + 1):
                        if j == 0:
                            if status[i-1] == '1':
                                status[i-1] = '0'
                            else:
                                status[i-1] = '1'
                        else:
                            if status[i-1-j] != status[i-1+j]:
                                break
                            else:
                                if status[i-1-j] == '1':
                                    status[i-1-j] = '0'
                                    status[i-1+j] = '0'
                                else:
                                    status[i-1-j] = '1'
                                    status[i-1+j] = '1'
            else:
                if i == number and number <= switch//2 + 1:
                    for j in range(number):
                        if j == 0:
                            if status[i-1] == '1':
                                status[i-1] = '0'
                            else:
                                status[i-1] = '1'
                        else:
                            if status[i-1-j] != status[i-1+j]:
                                break
                            else:
                                if status[i-1-j] == '1':
                                    status[i-1-j] = '0'
                                    status[i-1+j] = '0'
                                else:
                                    status[i-1-j] = '1'
                                    status[i-1+j] = '1'
                elif i == number and number > switch//2 + 1:
                    for j in range(switch - number + 1):
                        if j == 0:
                            if status[i-1] == '1':
                                status[i-1] = '0'
                            else:
                                status[i-1] = '1'
                        else:
                            if status[i-1-j] != status[i-1+j]:
                                break
                            else:
                                if status[i-1-j] == '1':
                                    status[i-1-j] = '0'
                                    status[i-1+j] = '0'
                                else:
                                    status[i-1-j] = '1'
                                    status[i-1+j] = '1'
print(status)

# for

print(' '.join(status))