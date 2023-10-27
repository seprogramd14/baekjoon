from functools import cmp_to_key
def compare(x, y):
    if x + y > y + x:
        return -1
    if x + y == y + x:
        return 0
    else:
        return 1

n = int(input())
num = list(map(str, input().split()))
num.sort(key = cmp_to_key(compare))
print(''.join(num) if int(''.join(num)) != 0 else 0)