n = int(input())

def Sum(num):
  result = 0
  for i in str(num):
    result += int(i)
  return result

res = 0

for i in range(1, n+1):
  i_re = Sum(i)
  if n == i + i_re:
    res = i
    break
print(res)