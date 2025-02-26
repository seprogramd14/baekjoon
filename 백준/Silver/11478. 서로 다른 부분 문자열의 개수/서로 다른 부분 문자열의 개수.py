import sys
input = sys.stdin.readline

s = input()
word = set()

for i in range(1, len(s)):
    for j in range(len(s)-i):
        word.add(s[j:j+i])
print(len(word))