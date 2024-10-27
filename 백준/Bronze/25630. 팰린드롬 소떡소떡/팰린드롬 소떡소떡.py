n = int(input())
s = input().rstrip()
if n % 2:
    print(sum([1 for f, s in zip(s[n//2-1::-1], s[n//2+1:]) if f != s]))
else:
    print(sum([1 for f, s in zip(s[n//2-1::-1], s[n//2:]) if f != s]))