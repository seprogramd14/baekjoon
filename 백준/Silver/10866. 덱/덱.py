from collections import deque
import sys
n = int(sys.stdin.readline())
dq = deque([])
for i in range(n):
    string = list(map(str, sys.stdin.readline().split()))
    if string[0] == 'push_front':
        dq.appendleft(string[1])
    elif string[0] == 'push_back':
        dq.append(string[1])
    elif string[0] == 'pop_front':
        print(dq.popleft() if dq else -1)
    elif string[0] == 'pop_back':
        print(dq.pop() if dq else -1)
    elif string[0] == 'size':
        print(len(dq))
    elif string[0] == 'empty':
        print(0 if dq else 1)
    elif string[0] == 'front':
        print(dq[0] if dq else -1)
    elif string[0] == 'back':
        print(dq[-1] if dq else -1)