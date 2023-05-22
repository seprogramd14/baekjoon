from collections import deque
def solution(prio, loc):
    answer = 0
    prio = deque(prio)
    while prio:
        max_prio = max(prio)
        p = prio.popleft()
        if p >= max_prio:
            answer += 1
            if loc == 0: break
            else: loc = len(prio) - 1 if loc <= 0 else loc - 1
        else:
            prio.append(p)
            loc = len(prio) - 1 if loc <= 0 else loc - 1
        print(loc)
    return answer