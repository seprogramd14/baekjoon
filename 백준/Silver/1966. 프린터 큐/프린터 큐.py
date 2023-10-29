import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for t in range(T):
    m, n = list(map(int, input().split())) # 문서 개수 / 원하는 인덱스
    queue = deque(list(map(int, input().split()))) # 중요도
    count = 0
    while queue:
        if max(queue) == queue[0]:
            count += 1
            if n == 0:
                break
            else:
                n = n-1 if n > 0 else len(queue) - 1
                queue.popleft()
        else:
            n = n-1 if n > 0 else len(queue) - 1
            queue.append(queue.popleft())
        
    print(count)