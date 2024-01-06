import sys
input = sys.stdin.readline

n = int(input())

if ((n - 1) // 4) % 2 != 0: # 1 2 3 4
    print(2 if n % 4 == 0 else 6 - n%4)
else: # 5 4 3 2
    print(4 if n % 4 == 0 else n%4)