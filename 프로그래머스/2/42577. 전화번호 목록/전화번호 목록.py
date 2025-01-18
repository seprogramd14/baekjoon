def solution(phone_book):
    dic = {b:0 for b in phone_book}
    for l in set([len(b) for b in phone_book]):
        for b in phone_book:
            if len(b) > l and b[:l] in dic.keys():
                return False
    return True