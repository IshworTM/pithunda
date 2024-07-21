from datetime import datetime, timedelta, date
import calendar

def _get_days_in_year():
    """this function actually works

    Returns:
        list: returns a lisst of days that are taken from a starting date of the same year
    """
    period_start = datetime(2024, 3, 18, 9, 30, 00)
    period_stop = datetime(2024, 3, 18, 10, 30, 00)
    year = period_start.year
    print("Year: ", year)
    start_hour = period_start.hour
    start_minute = period_start.minute
    start_second = period_start.second
    print("Start Hour :", start_hour)
    print("Start Minute :", start_minute)
    print("Start Second :", start_second)

    stop_hour = period_stop.hour
    stop_minute = period_stop.minute
    stop_second = period_stop.second
    print("stop_hour :", stop_hour)
    print("stop_minute :", stop_minute)
    print("stop_second :", stop_second)
    week_day = period_start.strftime('%A').upper()
    print("Week Day:", week_day)
    start_date = datetime(year, 1, 1, 00, 00, 00)
    print("Start Date weekday: ", start_date.weekday())
    days = []
    while start_date.year == year:
        if start_date.weekday() == calendar.weekday(year, 1, 1) + (getattr(calendar, week_day)):
            days.append({start_date + timedelta(hours=start_hour, minutes=start_minute, seconds=start_second) : start_date + timedelta(hours=stop_hour, minutes=stop_minute, seconds=stop_second)})
            start_date += timedelta(days=7)
        else:
            start_date += timedelta(days=1)
            
    for dictionary in days:
        for key, value in dictionary.items():
            print(key)
            print(value)
            print("Duration: ", (value-key).seconds//3600)
            
print(_get_days_in_year())