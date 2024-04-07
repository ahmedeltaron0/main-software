from datetime import datetime

def get_time():
    arabic_numbers = str.maketrans('0123456789', '٠١٢٣٤٥٦٧٨٩')
    
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    
    # Determine AM or PM and adjust hour for 12-hour format
    if hour >= 12:
        period = "مساءً"
        if hour > 12:
            hour -= 12
    else:
        period = "صباحًا"
        if hour == 0:
            hour = 12
    
    # Translate to Arabic numerals
    hour_ar = str(hour).translate(arabic_numbers)
    minute_ar = str(minute).translate(arabic_numbers)
    second_ar = str(second).translate(arabic_numbers)
    
    return f"الساعة الآن {hour_ar} {period} و {minute_ar} دقيقة و {second_ar} ثانية"

