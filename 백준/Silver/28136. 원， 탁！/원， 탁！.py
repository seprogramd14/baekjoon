n = int(input())
plate = list(map(int, input().split()))
cnt = 0
stack = []
for p in plate:
    if not stack:
        stack.append(p)
    elif stack[-1] < p:
        stack.append(p)
    else:
        stack = [p]
        cnt += 1
if stack and stack[-1] >= plate[0]:
    cnt += 1
print(cnt)