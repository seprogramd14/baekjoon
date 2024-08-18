import sys
input = sys.stdin.readline
dic = "XYZABCDEFGHIJKLMNOPQRSTUVW"

s = ''
for i in input().rstrip():
    s += dic[ord(i) - ord('A')]

print(s)
