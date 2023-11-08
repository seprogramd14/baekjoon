from collections import deque
import sys
input = sys.stdin.readline
T = int(input())

for t in range(T):
    commands = list(input().rstrip())
    n = int(input())
    numbers = deque(eval(input()))
    r, error = 0, 0
    for command in commands:
        if command == 'R':
            r += 1
        elif command == 'D':
            if not numbers:
                error = 1
                break
            if r % 2 == 0:
                numbers.popleft()
            else:
                numbers.pop()

    numbers = list(numbers)

    if error:
        print("error")
        continue
    if r % 2 == 0:
        print('[', end='')
        print(*numbers, sep=',', end='')
        print(']')
    else:
        print('[', end='')
        print(*numbers[::-1], sep=',', end='')
        print(']')