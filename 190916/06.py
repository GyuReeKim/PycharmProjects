# 암호코드 스캔
# 연습코드

code = ['3211', '2221', '2122', '1411', '1132', '1231', '1114', '1312', '1213', '3112']
binary = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
password = '196EBC5A316C578'

result = ''
for i in range(len(password)):
    if '0' <= password[i] <= '9':
        digit = ord(password[i]) - ord('0')
    else:
        digit = ord(password[i]) - ord('A') + 10
    for j in range(len(binary)):
        if digit == j:
            result += binary[j]
print(len(result), result)

if len(result) <= 60:
    for i in range(len(result)-1, -1, -1):
        if result[i] == '1':
            result = result[i-55:i+1]
            break
elif 60 < len(result) <= 120:
    for i in range(len(result)-1, -1, -1):
        if result[i] == '1':
            result = result[i-111:i+1]
            break
elif 120 < len(result) <= 300:
    for i in range(len(result)-1, -1, -1):
        if result[i] == '1':
            result = result[i-179:i+1]
            break
print(len(result), result)