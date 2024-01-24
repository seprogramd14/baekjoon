import sys
from collections import deque
input = sys.stdin.readline

n, k = list(map(int, input().split()))
check = [-1 for _ in range(100001)]
check[n] = 0
queue = deque([n])

while check[k] == -1:
    node = queue.popleft()
    ls = [i for i in [node-1, node+1, node*2] if 0 <= i <= 100000 and check[i] == -1]
    for l in ls:
        if check[l] == -1:
            check[l] = check[node] + 1
    queue.extend(ls)

print(check[k])