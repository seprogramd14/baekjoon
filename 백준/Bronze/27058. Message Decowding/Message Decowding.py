secret = input().rstrip()
ori = 'abcdefghijklmnopqrstuvwxyz'
key = {k:v for k, v in zip(ori + ori.upper(), secret + secret.upper())}
key[' '] = ' '
for i in input().rstrip():
    print(key[i], end='')