def add_time(start, duration, weekday=None):
    start_time, pm = start.split()
    time_hour, time_minute = [int(x) for x in start_time.split(':')]
    if pm == 'PM':
        time_hour = time_hour + 12
    duration_hour, duration_minute = [int(x) for x in duration.split(':')]

    # add minutes
    time_hour += (time_minute + duration_minute) // 60
    time_minute += duration_minute - 60 * ((time_minute + duration_minute) // 60)

    # add hours
    days = (time_hour + duration_hour) // 24
    time_hour += duration_hour - 24 * ((time_hour + duration_hour) // 24)
    new_pm = 'AM'
    if time_hour > 11:
        time_hour -= 12
        new_pm = 'PM'
        
    time_hour = 12 if time_hour == 0 else time_hour

    new_weekday = None
    if weekday:
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        index = weekdays.index(weekday.capitalize())
        index += days - 7 * ((index + days) // 7)
        new_weekday = weekdays[index]

    new_time = f'{str(time_hour)}:{str(time_minute).zfill(2)} {new_pm}'
    if weekday:
        new_time += f', {new_weekday}'
    if days:
        new_time += f' ({"next day" if days == 1 else str(days) + " days later"})'

    return new_time
