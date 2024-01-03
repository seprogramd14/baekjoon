import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == "#":
        break
    aeiou = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    cnt = 0
    for w in aeiou:
        cnt += s.count(w)
    print(cnt)