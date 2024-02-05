import sys, heapq
input = sys.stdin.readline

n = int(input())
time = sorted([list(map(int, input().split())) for _ in range(n)])
last = []
heapq.heappush(last, time[0][1])

for i in range(1, n):
    if last[0] <= time[i][0]:
        heapq.heappushpop(last, time[i][1])
    else:
        heapq.heappush(last, time[i][1])
print(len(last))