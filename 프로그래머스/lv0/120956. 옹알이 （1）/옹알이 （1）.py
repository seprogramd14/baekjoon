def solution(babbling):
    babb = ['aya', 'ye', 'woo', 'ma']
    answer = []
    for i in babbling:
        for b in babb:
            i = i.replace(b, '1')
        answer.append(i.replace('1', ''))
    return answer.count('')