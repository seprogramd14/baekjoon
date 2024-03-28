import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))
number.reverse()
stack = []
i = 1

while i <= n:
    if number and number[-1] == i:
        number.pop()
        i += 1
    elif stack and stack[-1] == i:
        stack.pop()
        i += 1
    else:
        if number:
            stack.append(number.pop())
        elif stack[-1] != i:
            break

if not stack:
    print("Nice")
else:
    print("Sad")