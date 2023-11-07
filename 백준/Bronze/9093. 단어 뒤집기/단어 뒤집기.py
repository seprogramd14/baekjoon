n = int(input())
for i in range(n):
    string = list(map(list, input().split()))
    for j in range(len(string)):
        print("".join(s for s in string[j][::-1]), end=" ")