while True:
  stack = []
  string = input()
  if string == '.': break
  if '(' not in string and ')' not in string and '[' not in string and ']' not in string:
      print('yes')
      continue
  for i in string:
    if i == '(' or i == '[': stack.append(i) # 완료
    elif i == ')':
      if stack and stack[len(stack)-1] == '(': stack.pop()
      else:
        stack.append(i)
        break
    elif i == ']':
      if stack and stack[len(stack)-1] == '[': stack.pop()
      else:
        stack.append(i)
        break
  print('no' if stack else 'yes')