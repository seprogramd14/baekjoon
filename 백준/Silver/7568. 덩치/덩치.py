T = int(input())
result = []
w_h = []
for t in range(T):
    w, h = input().split()
    w_h.append((int(w), int(h)))

for i in range(len(w_h)):
    rank = 1
    for j in range(len(w_h)):
        if w_h[i][0] < w_h[j][0] and w_h[i][1] < w_h[j][1]:
            rank += 1
        
    result.append(rank)

for i in result:
    print(i, end=' ')
