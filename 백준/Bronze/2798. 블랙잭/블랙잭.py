n, num = map(int, input().split())

card = list(map(int, input().split()))
max = 0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if num >= card[i]+ card[j] + card[k] and max < card[i]+ card[j] + card[k]:
                max = card[i]+ card[j] + card[k]

print(max)