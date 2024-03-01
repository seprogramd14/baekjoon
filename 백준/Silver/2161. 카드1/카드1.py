from collections import deque

n = int(input())
cards = deque([i for i in range(1, n+1)])
res = list()
i = 0

while len(cards) > 1:
    if i % 2: # 홀수
        cards.append(cards.popleft())
    else:
        res.append(cards.popleft())
    i += 1

print(*res, cards[0])