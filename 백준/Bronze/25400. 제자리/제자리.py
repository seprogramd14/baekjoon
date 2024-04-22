import sys
input = sys.stdin.readline
n = int(input())
card = list(map(int, input().split()))
sort_card = sorted(card)

if 1 not in sort_card:
    print(len(card))
    exit()
count = 0
fix = 0
while fix != len(card):
    for i in range(fix, len(card)):
        if i + 1 == card[i]:
            fix += 1
            break
        else:
            card = card[:fix] + card[fix+1:]
            count += 1
print(count)