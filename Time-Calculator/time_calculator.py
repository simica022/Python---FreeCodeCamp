def add_time(start_time, added_time, day=False):
  
days ={'Monday' : 0,
          'Tuesday' : 1,
          'Wednesday' : 2,
          'Thursday' : 3,
          'Friday' : 4,
          'Saturday' : 5,
          'Sunday' : 6}

    def convert_str_to_int(strs):
        return list(map(int, strs.split()[0].split(':')))

    def get_added_time(num, divider = 60):
        return num // divider 

    def convert_time_format(hour):
        if "PM" in hour.split():
            return 12
        return 0
    
    def add_zero(num):
        if num > 9:
            return str(num)
        return "0" + str(num)
    
    def return_pm_am(num):
        if num > 11:
            return "PM"
        return "AM"
    
    def adjust_hour_output(num):
        if num > 12:
            return str(num - 12)
        return str(num)

    def check_day(day):
        if day:
            return True
        return False

    def get_day_name(day):
        if not day:
            return 'Monday'
        return day.capitalize()

    def check_weekday(num):
        if num > 7:
            return num // 7 - 1
        return num
    st_hour, st_min = convert_str_to_int(start_time)
    st_hour = st_hour + convert_time_format(start_time)
    add_hour, add_min = convert_str_to_int(added_time)
    st_day = get_day_name(day)
    st_day_index = days[st_day]

    f_min = st_min + add_min - 60 * get_added_time(st_min + add_min)
    f_hour = get_added_time(st_min + add_min) + st_hour + add_hour

    num_of_days = st_day_index + get_added_time(f_hour, 24)
    f_day = list(days.keys())[check_weekday(num_of_days)]

    f_hour = f_hour - 24 * get_added_time(f_hour, 24)
    f_min = add_zero(f_min) + " " + return_pm_am(f_hour)
    f_hour = adjust_hour_output(f_hour)

    day_diff = num_of_days - st_day_index


    if not check_day(day) and day_diff == 0:
        time = f_hour + ":" + f_min
        return time

    if not check_day(day) and day_diff == 1:
        return f_hour + ":" + f_min + " " + "(next day)"

    if not check_day(day) and day_diff > 1:
        return f_hour + ":" + f_min + " " + f"({day_diff} days later)"

    if check_day(day) and day_diff == 0:
        return f_hour + ":" + f_min + " " + f_day
    
    if check_day(day) and day_diff == 1:
        return f_hour + ":" + f_min + " " + f_day + " " + "(next day)"
    
    if check_day(day) and day_diff > 1:
        return f_hour + ":" + f_min + " " + f_day + " " + f"({day_diff} days later)"
