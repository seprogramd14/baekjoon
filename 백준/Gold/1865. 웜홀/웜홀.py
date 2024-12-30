import sys
input = sys.stdin.readline

#벨만 포드 알고리즘 수행
def bellman_ford(start):
    table = [5001*10000] * (n+1)
    table[start] = 0
    
    for i in range(n):
        for s, e, t in edges:
            if table[s] != float("inf") and table[e] > table[s] + t:
                table[e] = table[s] + t # 최단 거리 갱신
                if i == n-1:
                    return 1
    return 0

for _ in range(int(input())):
    n, m, w = map(int, input().split())
    edges = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append([s, e, t])
        edges.append([e, s, t])
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append([s, e, -t])

    if bellman_ford(1):
        print("YES")
    else:
        print("NO")
