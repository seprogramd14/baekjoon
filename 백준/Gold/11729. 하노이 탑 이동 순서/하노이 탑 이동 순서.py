import sys
input = sys.stdin.readline

n = int(input())
answer = []
def hanoi(N, start, mid, end):
    if N == 1:
        answer.append([start, end])
    else:
        hanoi(N-1, start, end, mid) # 중간 경유지(2번, mid)로 이동
        answer.append([start, end]) # 목적지(3번, end)가 비어있으니 이동
        hanoi(N-1, mid, start, end) # 목적지(3번, end)로 이동

hanoi(n, 1, 2, 3)
print(len(answer))
for a in answer:
    print(*a)