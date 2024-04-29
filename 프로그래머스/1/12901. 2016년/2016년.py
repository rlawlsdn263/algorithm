import datetime

def solution(a, b):
    weekday = datetime.datetime(2016, a, b).weekday()
    weekday_str = ['MON', 'TUE', 'WED', 'THU','FRI', 'SAT', 'SUN']

    return weekday_str[weekday]
           