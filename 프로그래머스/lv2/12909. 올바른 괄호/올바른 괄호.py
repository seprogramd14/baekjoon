def solution(s):
    answer = True
    stack = []
    for w in s:
        if w == ')': stack.pop() if stack else stack.append(w)
        elif w == '(': stack.append(w)
    return False if stack else True