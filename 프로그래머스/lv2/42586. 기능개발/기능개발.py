from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    completions = deque([])
    for i in range(len(speeds)):
        completions.append(math.ceil((100 - progresses[i]) / speeds[i]))
    while completions:
        completion_front = completions.popleft()
        cut = 1
        while completions:
            if completion_front >= completions[0]:
                completions.popleft()
                cut += 1
            else: break
        answer.append(cut)
    return answer