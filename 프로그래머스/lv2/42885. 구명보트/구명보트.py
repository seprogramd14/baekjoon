from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while people:
        if len(people) >= 2 and people[0] + people[-1] <= limit:
            people.popleft()
        answer += 1
        people.pop()
    return answer
