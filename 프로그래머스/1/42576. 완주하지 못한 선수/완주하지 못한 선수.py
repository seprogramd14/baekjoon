from collections import Counter
def solution(participant, completion):
    count = Counter(participant)
    for i in completion:
        count[i] -= 1
    return [c for c in count if count[c]][0]