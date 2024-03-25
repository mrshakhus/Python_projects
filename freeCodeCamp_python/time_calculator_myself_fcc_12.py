'''
Write a function named add_time that takes in two required parameters and one optional parameter:

 - a start time in the 12-hour clock format (ending in AM or PM)
 - a duration time that indicates the number of hours and minutes
 - (optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.
'''
#add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

#add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

#add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

#add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

#add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

#add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)

def add_time(start, duration, week_day = None):

    #Extracting hours and minutes from strings
    time = start.split()[0]
    ampm_initial = start.split()[1]
    ampm_new = ''

    hours = time.split(':')[0]
    minutes = time.split(':')[1]
    hours = int(hours)
    minutes = int(minutes)

    duration_hours = duration.split(':')[0]
    duration_minutes = duration.split(':')[1]
    duration_hours = int(duration_hours)
    duration_minutes = int(duration_minutes)

    hours_from_minutes = int((minutes + duration_minutes)/60)

    if hours_from_minutes:
        minutes = (minutes + duration_minutes) % 60
    else:
        minutes = minutes + duration_minutes

    days_passed = int((duration_hours)/24)
    cycles_of_12 = int((hours + duration_hours + hours_from_minutes)/12)
    new_time_hours = (hours + duration_hours + hours_from_minutes) % 12
     
    if cycles_of_12 % 2 != 0:
        if ampm_initial == 'AM':
            ampm_new = 'PM'
        else:
            ampm_new = 'AM' 
    ampm_new = ampm_initial

    new_time = str(new_time_hours) + ":" + str(minutes).rjust(2,'0') + f' {ampm_new}'
    
    text_days_later = ''
    if days_passed == 0 and ampm_initial == 'PM' and ampm_new == 'AM':
        text_days_later = ' (next day)'
    elif days_passed == 0:
        text_days_later = ''
    else:
        text_days_later = f' ({days_passed} days later)'
    
    new_time += text_days_later
        

    return new_time

#print(add_time('3:30 PM', '2:12')) #1
print(add_time('11:55 AM', '3:12')) #2