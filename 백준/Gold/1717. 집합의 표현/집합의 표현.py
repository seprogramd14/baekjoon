import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

for _ in range(m):
    isfind, a, b = list(map(int, input().split()))
    
    if isfind:
        if find(a) == find(b): # 같은 부모를 가리키는 지 확인
            print('YES')
        else:
            print('NO')
    else:
        union(a, b) # 원소 합치기