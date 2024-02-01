import sys
input = sys.stdin.readline

s = input().rstrip().split('-')
ls = []
for i in range(len(s)):
    s[i] = s[i].split('+')
    count = 0
    for num in s[i]:
        count += int(num)
    ls.append(count)

for i in range(len(ls) - 1):
    ls[i+1] = ls[i] - ls[i+1]
print(ls[-1])