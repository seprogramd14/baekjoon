from collections import deque
def solution(bridge_length, weight, truck):
    answer, last, count = 0, 0, 0
    queue, truck = deque([]), deque(truck)
    while truck:
        if len(queue) >= bridge_length:
            count -= queue[0]
            queue.popleft()
        if queue and count + truck[0] > weight:
            queue.append(0)
            last -= 1
        else:
            queue.append(truck.popleft())
            count += queue[-1]
            last = bridge_length
        answer += 1
    return answer + last