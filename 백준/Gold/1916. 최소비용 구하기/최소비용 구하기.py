import heapq, sys
input = sys.stdin.readline

INF = 1e+9
n = int(input())
graph = {i+1:[] for i in range(n)}
for _ in range(int(input())):
    s, e, v = map(int, input().split())
    graph[s].append([e, v])

def dijkstra(start, end):
    heap = [[0, start]]
    distance = [INF] * (n+1)
    distance[start] = 0

    while heap:
        d, node = heapq.heappop(heap)
        if distance[node] < d:
            continue
        
        for e, v in graph[node]:
            if distance[e] > distance[node] + v:
                distance[e] = distance[node] + v
                heapq.heappush(heap, [d+v, e])

    return distance[end]

s, e = map(int, input().split())
print(dijkstra(s, e))