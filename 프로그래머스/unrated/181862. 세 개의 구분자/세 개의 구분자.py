def solution(mystr):
    mystr = mystr.translate(str.maketrans('abc', '   ')).split(' ')
    mystr = [i for i in mystr if i]
    return mystr if mystr else ["EMPTY"]