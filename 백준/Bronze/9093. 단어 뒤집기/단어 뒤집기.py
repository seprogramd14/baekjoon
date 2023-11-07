n = int(input())

for i in range(n):
  string = list(map(list, input().split()))
  for j in range(len(string)):
    string[j].reverse()
    print("".join(s for s in string[j]), end=" ")