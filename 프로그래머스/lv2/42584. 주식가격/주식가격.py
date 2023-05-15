from collections import deque

def solution(prices):
    answer = []
    prices_de = deque(prices)
    for i in range(len(prices)):
        pri = prices_de.popleft()
        cut = 0
        for j in prices_de:
            if pri <= j: cut += 1
            else:
                cut += 1
                break
        answer.append(cut)
    return answer