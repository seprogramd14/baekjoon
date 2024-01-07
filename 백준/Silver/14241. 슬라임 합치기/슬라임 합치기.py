import sys
input = sys.stdin.readline

n = int(input())
slime = sorted(list(map(int, input().split())))

size = [slime[0]]
score = 0
for i in range(1, n):
    p = size.pop()
    size.append(p + slime[i])
    score += p * slime[i]
print(score)