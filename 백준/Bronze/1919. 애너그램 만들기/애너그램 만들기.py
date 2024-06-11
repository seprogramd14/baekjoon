from collections import Counter
import sys
input = sys.stdin.readline

string = input().rstrip()
check = Counter(input().rstrip())
cnt = 0
for s in string:
    if s in check.keys() and check[s]:
        check[s] -= 1
    else:
        cnt += 1
print(cnt + sum(check.values()))