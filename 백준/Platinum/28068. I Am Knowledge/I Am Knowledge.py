import sys
input = sys.stdin.readline

n = int(input())

book_fun1, book_fun2 = [], []

for _ in range(n):
    a,  b = map(int, input().split())

    if a > b:
        book_fun2.append((a, b))
    else: # a <= b
        book_fun1.append((a, b))

book_fun1.sort()
book_fun2.sort(reverse=True, key=lambda x: x[1])

answer, result = 1, 0

for idx, fun in book_fun1+book_fun2:
    result -= idx
    if result < 0:
        answer = 0
        break
    result += fun

print(answer)