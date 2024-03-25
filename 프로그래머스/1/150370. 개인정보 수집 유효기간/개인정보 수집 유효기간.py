'''
1. 각 개인정보를 언제 저장했는지 for문으로 확인
2. for문으로 확인하면서 오늘 날짜와 비교 (~ 달로 비교)
# 주의 모든 달은 28일이다.
3. 비교 후 약관을 확인 후 유효기간이 지났는지 확인
4. 유효기간이 지났다면 결과에 저장
'''

# datetime 이용해보기
def solution(today, terms, privacies):
    answer = []
    today = today.split('.')
    dic = dict()
    for term in terms:
        dic[term[0]] = int(term[2:])
    
    for idx, p in enumerate(privacies):
        p = p.split()
        p[0] = p[0].split('.')
        y = int(today[0]) - int(p[0][0])
        m = int(today[1]) - int(p[0][1]) + y*12
        d = int(today[2]) - int(p[0][2])
        if d < 0:
            m -= 1
            d += 28
        if dic[p[1]] <= m:
            answer.append(idx+1)
    return answer