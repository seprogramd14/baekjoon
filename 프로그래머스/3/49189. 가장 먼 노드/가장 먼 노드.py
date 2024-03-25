'''
return : 1번 노드에서 가장 많이 떨어진 노드의 개수
# 해결 방안 : bfs 사용 (너비 우선 탐색)
1. 주어진 간선을 리스트로 표현한다.
2. 1번 노드부터 시작해서 bfs를 이용해 거리를 찾아간다.
# 이 때 visited 리스트를 이용해서 각 노드가 1로부터 얼마나 떨어졌는지 확인한다.
# visited 형태 : deque([현재 노드, 전 노드])
3. 가장 높은 숫자가 몇 개 있는지 검사한다.
'''


from collections import deque

def bfs(graph, start, n):
    queue = deque([[start, 0]])
    visited = [0] * (n+1)
    while queue:
        node, last = queue.popleft()
        if not visited[node]:
            visited[node] = visited[last] + 1
            for n in graph[node]:
                queue.append([n, node])
    return visited

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    result = bfs(graph, 1, n)
    answer = result.count(max(result))
    return answer