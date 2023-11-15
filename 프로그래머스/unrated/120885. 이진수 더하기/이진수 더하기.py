def solution(bin1, bin2):
    bin1, bin2 = int(bin1, 2), int(bin2, 2)
    return str(bin(bin1+bin2))[2:]