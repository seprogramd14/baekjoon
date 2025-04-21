def solution(schedules, timelogs, startday):
    deadlines = []
    for schedule in schedules:
        minutes = schedule%100+10
        hour = (schedule//100 + minutes//60) *100 
        deadlines.append(hour+minutes%60)
    
    answer = 0
    for deadline, timelog in zip(deadlines, timelogs):
        record = [True]*7
        for time in timelog:
            if startday not in [0, 6] and time > deadline:
                record[startday] = False
            startday = (startday+1)%7
        if all(record):
            answer += 1
    return answer