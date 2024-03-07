import datetime as dt

num = list(map(int, input().split()))
end = dt.datetime(2007, num[0], num[1])
weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
print(weekday[end.isoweekday() - 1])