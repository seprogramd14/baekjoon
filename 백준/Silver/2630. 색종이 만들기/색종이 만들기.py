import sys
input = sys.stdin.readline

answer = [0, 0]

def is_square(s_r, e_r, s_c, e_c):
    data = []
    for i in range(s_r, e_r):
        for j in range(s_c, e_c):
            data.append(paper[i][j])
    check = set(data)
    if len(check) == 1:
        answer[data[0]] += 1
        return 1
    else:
        return 0

def square(s_r, e_r, s_c, e_c):
    if not is_square(s_r, e_r, s_c, e_c):
        square(s_r, (s_r + e_r) // 2, s_c, (s_c + e_c) // 2) # 왼쪽 위
        square((s_r + e_r) // 2, e_r, s_c, (s_c + e_c) // 2) # 왼쪽 아래
        square(s_r, (s_r + e_r) // 2, (s_c + e_c) // 2, e_c) # 오른쪽 위
        square((s_r + e_r) // 2, e_r, (s_c + e_c) // 2, e_c) # 오른쪽 아래

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
l = len(paper)
square(0, l, 0, l)
print(answer[0])
print(answer[1])