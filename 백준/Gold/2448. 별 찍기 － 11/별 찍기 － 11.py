import sys
input = sys.stdin.readline

pattern = [[" ", " ", "*", " ", " "],
            [" ", "*", " ", "*", " "],
            ["*", "*", "*", "*", "*"]]

n = int(input())
star = [[" "] * (2*n-1) for _ in range(n)]

def triangle(t, start: list):
    if t == 3:
        for i in range(3):
            for j in range(5):
                star[start[0]+i][start[1]+j] = pattern[i][j]
        return 

    # 2. 세갈래로 삼각형 나누기
    triangle(t//2, [0+start[0], t//2+start[1]])
    triangle(t//2, [t//2+start[0], 0+start[1]])
    triangle(t//2, [t//2+start[0], t+start[1]])

triangle(n, [0, 0])

for r in star:
    print(*r, sep="")
