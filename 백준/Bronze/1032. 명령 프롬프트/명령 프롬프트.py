import sys
input = sys.stdin.readline

n = int(input())
sentence = [input().rstrip() for _ in range(n)]
result = ''

for i in range(len(sentence[0])):
    test = set()
    for j in range(n):
        test.add(sentence[j][i])
    if len(test) == 1:
        result += list(test)[0]
    else:
        result += '?'

print(result)