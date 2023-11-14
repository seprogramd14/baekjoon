import sys
input = sys.stdin.readline

brackets = list(input().rstrip())
stack = ['(']
count = 0

for i in range(1, len(brackets)):
    if brackets[i] == ')':
        stack.pop()
        if brackets[i-1] == '(':
            count += len(stack)
        elif brackets[i-1] == ')':
            count += 1
    elif brackets[i] == '(':
        stack.append('(')

print(count)