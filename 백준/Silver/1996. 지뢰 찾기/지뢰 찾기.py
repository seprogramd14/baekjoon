import sys
input = sys.stdin.readline

n = int(input())
Map = [[i for i in input().rstrip()] for _ in range(n)]
new_Map = [['0' for _ in range(n)] for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(n):
    for j in range(n):
        if Map[i][j].isalnum():
            new_Map[i][j] = '*'
            for d in range(8):
                _i, _j = i + dx[d], j + dy[d]
                if 0 <= _i < n and 0 <= _j < n and new_Map[_i][_j] != '*':
                    new_Map[_i][_j] = str(int(new_Map[_i][_j]) + int(Map[i][j]))

for i in range(n):
    for j in range(n):
        if new_Map[i][j] != '*' and int(new_Map[i][j]) >= 10:
            new_Map[i][j] = "M"

for m in new_Map:
    print(''.join(m))