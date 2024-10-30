import sys
input = sys.stdin.readline

num = int(input())
result = []
for x in range(-200, 201):
    a = x * 508 if x > 0 else -x * 108
    for y in range(-200, 201):
        b = y * 212 if y > 0 else -y * 305
        if (a+b)*4763 == num:
            result.append([abs(x), abs(y)])

result.sort(key=lambda x: (x[0], x[1]))
print(len(result))
for r in result:
    print(*r)