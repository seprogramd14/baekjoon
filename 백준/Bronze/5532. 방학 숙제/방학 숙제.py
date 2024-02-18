from math import ceil

l = int(input())
ls = [int(input()) for _ in range(4)]
korean = ceil(ls[0] / ls[2])
math = ceil(ls[1] / ls[3])
print(l - max(korean, math))