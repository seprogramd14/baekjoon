# 우선순위 큐
import heapq
from sys import stdin
heap = []
result = []
n = int(input())

for A in stdin:
  if int(A) > 0:
    heapq.heappush(heap, int(A))
  else:
    if heap: result.append(heapq.heappop(heap))
    else: result.append(0)
for i in result:
  print(i)