import sys
input = sys.stdin.readline

n, m  = list(map(int, input().split()))
area = [[i for i in input().rstrip()] for i in range(n)]

dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

for i in range(n):
    for j in range(m):
        if area[i][j] == "W":
            for k in range(4):
                i_c, j_c = i + dy[k], j + dx[k]
                if 0 <= i_c < n and 0 <= j_c < m:
                    if area[i_c][j_c] == "S":
                        print(0)
                        exit()

print(1)
for i in area:
    print(''.join(i).replace('.', 'D'))