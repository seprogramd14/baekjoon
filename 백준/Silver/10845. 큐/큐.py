from collections import deque
import sys
queue = deque([])
n = int(sys.stdin.readline())
result = []
for i in range(n):
  string = input()
  if string == 'pop':
    result.append(queue.popleft() if queue else '-1')
  elif string == 'size':
    result.append(len(queue))
  elif string == 'empty':
    result.append('1' if len(queue) == 0 else '0')
  elif string == 'front':
    result.append(queue[0] if len(queue) != 0 else '-1')
  elif string == 'back':
    result.append(queue[-1] if len(queue) != 0 else '-1')
  else:
    queue.append(string[5:])

for i in result:
  print(i)