def move(n, start, end):
    global answer
    answer.append([start, end])

def hanoi(n, start, end, mid):
    if n == 1:
        move(1, start, end)
    else:
        hanoi(n-1, start, mid, end)
        move(n, start, end)
        hanoi(n-1, mid, end, start)
answer = []    
def solution(n):
    hanoi(n, 1, 3, 2)
    return answer