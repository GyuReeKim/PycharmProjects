# 크기가 정해진 리스트를 사용한 스택 구현
# 마지막에 저장된 메모리를 찾아 쓸 수 있으면 된다.
stack = [0]*10 # list의 range 오류 확인 가능하다.
top = -1

# push(1)
top = top + 1 # index가 0일때
stack[top] = 1 # stack[0]에 1을 저장
# push(2)
top = top + 1 # index가 1일때
stack[top] = 2 # stack[1]에 1을 저장
# push(3)
top = top + 1 # index가 2일때
stack[top] = 3 # stack[2]에 1을 저장

print(stack)

# pop()
r = stack[top]
top = top - 1
print(r)

while top != -1: # 스택이 비어있지 않으면 반복
    r = stack[top]
    top = top - 1
    print(r)

# append()를 사용한 스택
s = list()
s.append(10)
s.append(20)
s.append(30)
print(s)
while len(s) != 0:
    print(s.pop())
print(s)