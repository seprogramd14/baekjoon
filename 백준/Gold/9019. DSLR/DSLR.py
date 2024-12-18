import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def bfs(root, end):
    queue = deque([[root, ""]])
    visited = [0]*10001

    while queue:
        node, ope = queue.popleft()
        if node == end:
            print(ope)
            break
        else:
            L = node%1000*10 + node//1000
            if not visited[L]:
                visited[L] = 1
                queue.append([L, ope+"L"])

            R = node//10 + (node%10)*1000
            if not visited[R]:
                visited[R] = 1
                queue.append([R, ope+"R"])

            S = node-1 if node else 9999
            if not visited[S]:
                visited[S] = 1
                queue.append([S, ope+"S"])

            D = (node*2)%10000
            if not visited[D]:
                visited[D] = 1
                queue.append([D, ope+"D"])

for _ in range(t):
    a, b = map(int, input().split())
    bfs(a, b)