string = [input().rstrip() for _ in range(3)][::-1]

result = 0
for i in range(3):
    if string[i].isdigit():
        result = int(string[i]) + i+1
        break

if not result % 15:
    print('FizzBuzz')
elif not result % 3:
    print('Fizz')
elif not result % 5:
    print('Buzz')
else:
    print(result)