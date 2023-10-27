n, l = list(map(int, input().split()))
stack = []
num = ','.join(input()).split(',')
for i in num:
    if not stack:
        stack.append(i)
    else:
        while stack and str(i) + str(stack[-1]) > str(stack[-1]) + str(i) and l > 0:
            stack.pop()
            l -= 1
        stack.append(i)

for i in range(l):
    stack.pop()

print(''.join(stack))