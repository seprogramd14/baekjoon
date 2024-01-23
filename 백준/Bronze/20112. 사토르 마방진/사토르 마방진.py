import sys
input = sys.stdin.readline

n = int(input())
words = [[i for i in input().rstrip()] for _ in range(n)]

for i in range(n):
    s1 = ''.join(words[i])
    s2 = ''
    for word in words:
        s2 += word[i]
    
    if s1 != s2:
        print('NO')
        sys.exit()

print('YES')