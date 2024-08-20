s, e = map(int, input().split())
nums = [i**2 for i in range(1, 46)]
start, end = 0, 0

for i in range(1, 46):
    stand = i*(i+1) // 2
    if e <= stand:
        end = sum(nums[:i]) - (stand - e) * i
        break

for i in range(1, 46):
    stand = i*(i+1) // 2
    if s <= stand:
        start = sum(nums[:i]) - (stand - s) * i - i
        break

print(end - start)