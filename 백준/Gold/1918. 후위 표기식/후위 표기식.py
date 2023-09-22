op = input()
operating = {'*' : 10, '/' : 10, '+' : 2, '-' : 2, '(': 0}
word = ['*', '/', '+', '-']
stack = []

for i in op:
  if i == '(':
    stack.append(i)
  elif i == ')':
    while stack[-1] != '(':
      print(stack.pop(), end='')
    stack.pop() # 왼쪽괄호 제거
  elif i in word: # 연산자일 때
    if not stack: stack.append(i) # 안 들어있으면 그냥 넣기
    elif operating[stack[-1]] + 1 < operating[i]: # 마지막보다 우선순위 크면 넣기
      stack.append(i)
    else:
      while stack and operating[stack[-1]] + 1 > operating[i]:
        print(stack.pop(), end='')
      stack.append(i)
  else:
    print(i,end='')

while stack:
  print(stack.pop(), end="")