n = int(input())
string = list(input())
result = 0
for i in range(n):
    word_num = ord(string[i]) - 96
    result += word_num * (31**i)
print(result)