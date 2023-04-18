num = int(input())
word = [input() for _ in range(num)]
word = list(set(word))
wordtu = [(wo, len(wo)) for wo in word]
wordtu.sort(key= lambda x: (x[1], x[0]))
for wor in wordtu:
    print(wor[0])