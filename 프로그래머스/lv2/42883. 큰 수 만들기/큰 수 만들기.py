def solution(number, k):
    stack = []
    for i in range(len(number)):
        while stack and stack[-1] < number[i] and k != 0:
            stack.pop()
            k -= 1
        stack.append(number[i])
        
    return ''.join(stack) if k != 1 else number[:len(number)-1]