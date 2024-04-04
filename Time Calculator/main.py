def add_time(start, duration, start_day=None):
    
    # Parsing start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    
    # Parsing duration
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Convert start time to 24-hour format
    if period == 'PM':
        start_hour += 12
    
    # Calculate total minutes
    total_minutes = start_hour*60 + start_minute + duration_hour*60 + duration_minute
    
    # Calculate days and remaining minutes
    days = total_minutes // (24 * 60)
    remaining_minutes = total_minutes % (24 * 60)
    
    # Calculate new hour and minute #type: integer
    new_hour = remaining_minutes // 60 % 12
    new_minute = remaining_minutes % 60
    
    # Determine period (AM or PM) #type: string
    new_period = 'AM' if (remaining_minutes // 60) % 24 < 12 else 'PM' 
    
    # Adjust hour if it's 0
    if new_hour == 0:
        new_hour = 12
    else:
        new_hour = str(new_hour)
    
    # Determine day of the week if start_day is provided
    if start_day:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day_index = days_of_week.index(start_day.lower().capitalize())
        new_day_index = (start_day_index + days) % 7
        new_day = days_of_week[new_day_index]
        day_info = ', ' + new_day
    
    # Determine if it's next day or n days later
    if days == 0:
        days_info = ''
    elif days == 1:
        days_info = ' (next day)'
    else:
        days_info = ' (' + str(days) + ' days later)'
    
    # Constructing result # Convert new_hour to string first
    result = str(new_hour) + ':' + str(new_minute).zfill(2) + ' ' + new_period

    if start_day:
        result += day_info
    result += days_info
    print (result)
    return result

# Examples
# add_time('3:00 PM', '3:10')  # Output: 6:10 PM
# add_time('11:30 AM', '2:32', 'Monday')  # Output: 2:02 PM, Monday
# add_time('11:43 AM', '00:20')  # Output: 12:03 PM
# add_time('10:10 PM', '3:30')  # Output: 1:40 AM (next day)
# add_time('11:43 PM', '24:20', 'tueSday')  # Output: 12:03 AM, Thursday (2 days later)
# add_time('6:30 PM', '205:12')  # Output: 7:42 AM (9 days later)

add_time('3:30 PM', '2:12')
add_time('11:55 AM', '3:12')
add_time('2:59 AM', '24:00')
add_time('11:59 PM', '24:05')
add_time('8:16 PM', '466:02')
add_time('3:30 PM', '2:12', 'Monday')
add_time('2:59 AM', '24:00', 'saturDay')
add_time('11:59 PM', '24:05', 'Wednesday')
add_time('8:16 PM', '466:02', 'tuesday')
