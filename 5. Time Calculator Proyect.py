def add_time(start, duration, day=False):
    # Days of the week array and dictionary
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_index = {day.lower(): i for i, day in enumerate(days_of_week)}

    # Split start and duration times
    start_time, am_pm = start.split()
    start_hours, start_minutes = map(int, start_time.split(':'))
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Calculate new minutes and hours
    end_minutes = start_minutes + duration_minutes
    extra_hours = end_minutes // 60
    end_minutes %= 60

    end_hours = start_hours + duration_hours + extra_hours
    am_pm_flips = (end_hours // 12) % 2
    total_days = end_hours // 24
    end_hours = end_hours % 12 or 12  # 12-hour format

    # Determine final AM/PM
    if am_pm == 'PM' and (start_hours + duration_hours) >= 12:
        total_days += 1
    am_pm = 'PM' if (am_pm == 'AM' and am_pm_flips == 1) or (am_pm == 'PM' and am_pm_flips == 0) else 'AM'

    # Format end minutes and add final time
    end_minutes = f'{end_minutes:02}'
    final_time = f'{end_hours}:{end_minutes} {am_pm}'

    # Handle day of the week if provided
    if day:
        day = day.lower()
        end_day = days_of_week[(day_index[day] + total_days) % 7]
        final_time += f', {end_day}'

    # Append day or days later info
    if total_days == 1:
        final_time += ' (next day)'
    elif total_days > 1:
        final_time += f' ({total_days} days later)'

    return final_time
