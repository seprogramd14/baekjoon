error = r"1234567890-=wertyuiop[]\sdfghjkl;'xcvbnm,./"
ori = r"`1234567890-qwertyuiop[]asdfghjkl;zxcvbnm,."
key = {k:v for k, v in zip(error.upper(), ori.upper())}
key[' '] = ' '
while True:
    try:
        s = input().rstrip()
        for i in s:
            print(key[i], end='')
        print()
    except:
        break