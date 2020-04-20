import datetime

def change_time(const):
    current_time = datetime.datetime.now()
    second = current_time.second
    minute = current_time.minute
    hour = current_time.hour
    day = current_time.day
    month = current_time.month
    year = current_time.year
    second = second + const
    if second >= 60:
        minute = minute + second // 60
        second = second % 60
        if minute >= 60:
            hour = hour + minute // 60
            minute = minute % 60
            if hour >= 24:
                day = day + hour // 24
                hour = hour % 24
                while check_increased_day(day, month, year):
                    day = day - get_last_day(month, year)
                    month = month + 1
                    if month == 13:
                        year = year + 1
                        month = 1
    if second < 0:
        minute = minute - abs(second // 60)
        second = second % 60
        if minute < 0:
            hour = hour - abs(minute // 60)
            minute = minute % 60
            if hour < 0:
                day = day - abs(hour // 24)
                hour = hour % 24
                while day < 1:
                    day = day + get_last_day(month, year)
                    month = month - 1
                    if month == 0:
                        month = 12
                        year = year - 1
    return current_time.replace(year, month, day, hour, minute, second, 0)


def check_increased_day(day, month, year):
    return (day >= 30 and month == 2 and check_year(year)) or (day >= 29 and month == 2 and not check_year(year)) or (day >= 32 and month in (1, 3, 5, 7, 8, 10, 12)) or (day >= 31 and month in (4, 6, 9, 11))


def check_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def get_last_day(month, year):
    if month == 2:
        if check_year(year):
            return 29
        else:
            return 28
    if month in (1,3,5,7,8,10,12):
        return 31
    else:
        return 30

