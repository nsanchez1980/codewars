def format_duration(seconds):
    if seconds==0:
        return "now"
        
    years = 0
    days = 0
    hours = 0
    minutes = 0
    result = ""
    
    while seconds>=60:
        seconds = seconds - 60
        minutes = minutes + 1
    while minutes>=60:
        minutes = minutes - 60
        hours = hours + 1
    while hours>=24:
        hours = hours - 24
        days = days + 1
    while days>=365:
        days = days - 365
        years = years + 1
    
    if years>0:
        result = str(years) + " year"
        if years>1:
            result = result + "s"

    if days>0:
        if hours!=0 or minutes!=0 or seconds!=0:
            result = result + ", "
        else:
            result = result + " and "
        result = result + str(days) + " day"
        if days>1:
            result = result + "s"

    if hours>0:
        if minutes!=0 or seconds!=0:
            result = result + ", "
        else:
            result = result + " and "
        result = result + str(hours) + " hour"
        if hours>1:
            result = result + "s"

    if minutes>0:
        if seconds!=0:
            result = result + ", "
        else:
            result = result + " and "
        result = result + str(minutes) + " minute"
        if minutes>1:
            result = result + "s"

    if seconds>0:
        result = result + " and " + str(seconds) + " second"
        if seconds>1:
            result = result + "s"

    return result.lstrip(", ").lstrip(" and")



print(format_duration(29038299))
print(format_duration(1))
print(format_duration(62))
print(format_duration(120))
print(format_duration(3600))
print(format_duration(3662))