import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def bfs(i, j):
	visited = [[0 for _ in range(m)] for _ in range(n)]
	queue = deque([(i, j)])

	while queue:
		i, j = queue.popleft()
		cabbage[i][j] = 0

		dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

		for d in range(4):
			x, y = i + dx[d], j + dy[d]
			if 0 <= x < n and 0 <= y < m:
				if cabbage[x][y] == 1 and visited[x][y] != 1:
					visited[x][y] = 1
					queue.append((x, y))


for t in range(T):
	n, m, k = list(map(int, input().split()))
	cabbage = [[0 for _ in range(m)] for _ in range(n)]
	for i in range(k):
		x, y = list(map(int, input().split()))
		cabbage[x][y] = 1
	
	count = 0
	for i in range(n):
		for j in range(m):
			if cabbage[i][j] == 1:
				count += 1
				bfs(i, j)
	print(count)