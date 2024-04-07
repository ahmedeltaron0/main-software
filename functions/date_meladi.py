from datetime import datetime

def get_gregorian_date():
    # Arabic translations for month names
    months = {
        1: "يناير",
        2: "فبراير",
        3: "مارس",
        4: "أبريل",
        5: "مايو",
        6: "يونيو",
        7: "يوليو",
        8: "أغسطس",
        9: "سبتمبر",
        10: "أكتوبر",
        11: "نوفمبر",
        12: "ديسمبر"
    }
    
    # Function to translate numbers to Arabic
    def translate_to_arabic(n):
        arabic_numbers = str.maketrans('0123456789', '٠١٢٣٤٥٦٧٨٩')
        return str(n).translate(arabic_numbers)
    
    now = datetime.now()
    day = translate_to_arabic(now.day)
    month = months[now.month]
    year = translate_to_arabic(now.year)
    
    return f"اليوم هو {day} من {month} سنة {year}"
