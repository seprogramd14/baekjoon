num = int(input())

cnt = 1
while cnt * (cnt + 1) // 2 < num: cnt += 1
b = num - (cnt * (cnt - 1) // 2 + 1)
up, down = str(1 + b), str(cnt - b)
if not cnt % 2:
    print(up + '/' + down)
else:
    print(down + '/' + up)