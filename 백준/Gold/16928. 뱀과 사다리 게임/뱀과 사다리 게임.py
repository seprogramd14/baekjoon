import sys
from collections import deque
input = sys.stdin.readline

n, m = list(map(int, input().split()))
visited = [False] * 101
count = [0] * 101
ladder = dict()
snake = dict()

def bfs():
    queue = deque([1])
    while queue:
        node = queue.popleft()

        for i in range(1, 7):
            next = node + i
            if next <= 100 and not visited[next]:
                if next in ladder.keys():
                    next = ladder[next]
            
                if next in snake.keys():
                    next = snake[next]
                
                if not visited[next]:
                    visited[next] = True
                    count[next] = count[node] + 1
                    queue.append(next)
        if visited[-1]:
            break

for _ in range(n):
    x, y = list(map(int, input().split()))
    ladder[x] = y

for _ in range(m):
    v, u = list(map(int, input().split()))
    snake[v] = u

bfs()
print(count[-1])