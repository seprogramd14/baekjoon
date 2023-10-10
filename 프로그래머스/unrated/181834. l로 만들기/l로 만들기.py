import re
def solution(myString):
    return re.sub('a|b|c|d|e|f|g|h|i|j|k', 'l', myString)