from collections import deque
def solution(A, B):
    count = 0
    A = deque(A)
    for i in range(len(A)):
        if ''.join(list(A)) == B:
            break
        else:
            A.appendleft(A.pop())
            count += 1
    if len(A) == count: count = -1
    return count