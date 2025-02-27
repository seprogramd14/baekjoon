import sys
input = sys.stdin.readline

n = int(input())
matrics = [list(map(int, input().split())) for _ in range(n)]
paper = [0] * 3

def check_square(start, size):
    start_value = matrics[start[0]][start[1]]
    if size == 1:
        paper[start_value] += 1
        return 
    
    flat = []
    for i in range(start[0], start[0]+size):
        for j in range(start[1], start[1]+size):
            flat.append(matrics[i][j])
    
    if not [f for f in flat if f != start_value]:
        paper[start_value] += 1
    else:
        for i in range(start[0], start[0]+size, size//3):
            for j in range(start[1], start[1]+size, size//3):
                check_square([i, j], size//3)
check_square([0, 0], n)
print(*paper[-1:]+paper[:-1], sep="\n")