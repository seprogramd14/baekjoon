import math
def solution(fees, records):
    records = [r.split() for r in records]
    car_list = dict()
    result = dict()
    for record in records:
        record[0] = record[0].split(':')
        if record[2] == "IN":
            car_list[record[1]] = record[0]
            if record[1] not in result.keys():
                result[record[1]] = 0
        else: # 시간 계산
            time = car_list[record[1]]
            del car_list[record[1]]
            h, m = int(record[0][0]) - int(time[0]), int(record[0][1]) - int(time[1])
            result[record[1]] += (h * 60 + m)
    
    for car in car_list.keys(): # 남은 차량
        time = car_list[car]
        h, m = 23 - int(time[0]), 59 - int(time[1])
        result[car] += (h * 60 + m)
    answer = []
    for r in sorted(result.keys()):
        bonus = math.ceil((result[r] - fees[0])/fees[2])*fees[3] if result[r] > fees[0] else 0
        answer.append(fees[1] + bonus)
    return answer