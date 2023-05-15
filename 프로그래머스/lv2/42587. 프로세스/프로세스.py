from collections import deque

def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    while priorities:
        max_prio = max(priorities)
        prio = priorities.popleft()
        if prio >= max_prio:
            answer += 1
            if location == 0: break
            else: location = len(priorities) - 1 if location <= 0 else location - 1
        else:
            priorities.append(prio)
            location = len(priorities) - 1 if location <= 0 else location - 1
        print(location)
    return answer