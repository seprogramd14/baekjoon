import sys
input = sys.stdin.readline
S = input()
stack = [] # 처리
result = '' # 결과 저장
tag = 0 # 태그 확인

for word in S:
    if word == '<':
        while stack: result += stack.pop()
        stack = []
        tag = 1

    if tag == 1:
        result += word
    elif word == ' ' or word == '\n':
        while stack: result += stack.pop()
        if word == ' ':
            result += ' '
            stack = []
    else:
        stack.append(word)

    if '>' == word:
        tag = 0

print(result)