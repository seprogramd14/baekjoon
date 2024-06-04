import sys
import heapq
input = sys.stdin.readline
inf = float('inf')

n, m, p = map(int, input().split())
graph = {i : [] for i in range(1, n+1)}
for _ in range(m):
    v, u, w = map(int, input().split())
    graph[v].append([u, w]) # 끝점, 가중치

def d(start, end):
    table = [inf] * (n+1)
    table[start] = 0
    heap = [(0, start)] # 시작값 설정

    while heap:
        time, node = heapq.heappop(heap)

        if node == end:
            break

        for next_node, next_time in graph[node]:
            next_time += time
            if table[next_node] > next_time:
                table[next_node] = next_time
                heapq.heappush(heap, [next_time, next_node])
    return table[end]

result = []
for i in range(1, n+1):
    result.append(d(i, p) + d(p, i))
print(max(result))