from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    for i in range(len(prices)):
        pri = prices.popleft()
        cut = 0
        for j in prices:
            if pri <= j: cut += 1
            else:
                cut += 1
                break
        answer.append(cut)
    return answer
