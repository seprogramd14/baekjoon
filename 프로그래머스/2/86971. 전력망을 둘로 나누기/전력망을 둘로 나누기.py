def dfs(graph, start, root):
    stack = [start]
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited and node != root:
            stack.extend(graph[node])
            visited.append(node)
    return len(visited)

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    answer = []
    for wire in wires:
        a = dfs(graph, wire[0], wire[1])
        b = dfs(graph, wire[1], wire[0])
        answer.append(abs(a-b))
    return min(answer)