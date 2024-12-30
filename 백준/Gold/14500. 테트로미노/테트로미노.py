import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
dire = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 재귀 구현 - L, O, I, Z
def dfs(start, visited, total):
    if len(visited) == 3:
        result.append(total)
        return
    for x, y in dire:
        dx, dy = start[0]+x, start[1]+y
        if 0 <= dx < n and 0 <= dy < m:
            if [dx, dy] not in visited:
                dfs([dx, dy], visited+[start], total+paper[dx][dy])

result = []
for i in range(n):
    for j in range(m):
        dfs([i, j], [], paper[i][j])
        # 브루트포스 구현 - T
        check = []
        for x, y in dire:
            dx, dy = i+x, j+y
            if 0 <= dx < n and 0 <= dy < m:
                check.append(paper[dx][dy])
        if len(check) > 2:
            res = sum(check) + paper[i][j]
            result.append(res if len(check) == 3 else res - min(check))

print(max(result))
