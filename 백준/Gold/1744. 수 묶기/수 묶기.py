import sys
input = sys.stdin.readline

n = int(input())
num_list = [int(input()) for _ in range(n)]
plus = sorted([num for num in num_list if num > 0], reverse=True)
minus = sorted([num for num in num_list if num < 0])
zero = 0 in num_list

result = []
for i in range(1, len(plus), 2):
    if plus[i-1] == 1 or plus[i] == 1:
        result.extend([plus[i-1], plus[i]])
    else:
        result.append(plus[i-1] * plus[i])
for i in range(1, len(minus), 2):
    result.append(minus[i-1] * minus[i])

if len(minus) % 2 != 0 and not zero:
    result.append(minus[-1])
if len(plus) % 2 != 0:
    result.append(plus[-1])

result = sum(result)
print(result)