from collections import Counter
for _ in range(int(input())):
    num = Counter([int(input()) for _ in range(int(input()))])
    val = max(num.values())
    print(sorted([k for k in num if num[k] == val])[0])