import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))
stack, res = [1], [0]

for i in range(1, n):
    while stack and tower[stack[-1]-1] < tower[i]:
        stack.pop()
    res.append(stack[-1] if stack else 0)
    stack.append(i+1)
print(*res)