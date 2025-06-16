import sys
from collections import deque
input = sys.stdin.readline

student_num, compare_num = map(int, input().split())
graph = [[] for _ in range(student_num+1)]
indegree = [0] * (student_num+1)

for _ in range(compare_num):
    stu1, stu2 = map(int, input().split())
    graph[stu1].append(stu2)
    indegree[stu2] += 1

queue = deque([idx for idx, value in enumerate(indegree) if idx != 0 and not value])

result = []
while queue:
    node = queue.popleft()
    result.append(node)

    for g in graph[node]:
        indegree[g] -= 1
        if not indegree[g]:
            queue.append(g)
    print(node)

print(*result)