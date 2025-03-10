import sys
input = sys.stdin.readline

bucket = input().rstrip()
stack = []

result = 0
for i in range(len(bucket)):
    if bucket[i] == "(":
        stack.append(bucket[i])
    else:
        stack.pop()
        result += len(stack) if bucket[i-1] == "(" else 1
print(result)