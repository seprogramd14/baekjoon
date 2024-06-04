import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    v, u = map(int, input().split())
    tree[v].append(u)
    tree[u].append(v)

def search(start):
    stack = [start]
    table = {i : 0 for i in range(2, n+1)}
    while stack:
        node = stack.pop()
        for t in tree[node]:
            if t == 1:
                continue
            if not table[t]:
                stack.append(t)
                table[t] = node
    return table

result = search(1)

for value in result.values():
    print(value)