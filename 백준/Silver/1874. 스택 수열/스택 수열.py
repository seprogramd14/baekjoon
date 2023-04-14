import sys
input = sys.stdin.readline
n = int(input())
stack = [input().strip() for _ in range(n)]
result = []
res = []
lim = 1
for i in stack: # 4 3 6 8 7 5 2 1
  while len(stack) + 1 >= lim:
    if int(i) in result:
      result.pop()
      res.append('-')
      break
    else:
      result.append(lim)
      res.append('+')
      lim += 1
if result: print('NO')
else:
  for i in res:
    print(i)