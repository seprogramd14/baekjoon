import sys
input = sys.stdin.readline

word = input().rstrip()
save = []

for i in range(len(word)-2):
    for j in range(i+1, len(word)-1):
        save.append(word[i::-1] + word[j:i:-1] + word[:j:-1])

save.sort()
print(save[0])