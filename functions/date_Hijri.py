from hijri_converter import Gregorian
import datetime

def number_to_arabic(number):
    # Define mapping for Arabic numerals
    arabic_numerals = {
        '0': '٠',
        '1': '١',
        '2': '٢',
        '3': '٣',
        '4': '٤',
        '5': '٥',
        '6': '٦',
        '7': '٧',
        '8': '٨',
        '9': '٩'
    }
    # Convert each digit to Arabic numeral
    return ''.join(arabic_numerals[digit] for digit in str(number))

def get_hijri_date():
    current_date = datetime.datetime.now()
    year = current_date.year
    month = current_date.month
    day = current_date.day
    
    # Convert Gregorian date to Hijri
    hijri_date = Gregorian(year, month, day).to_hijri()
    
    # Define Arabic month names
    arabic_months = [
        "محرم", "صفر", "ربيع الأول", "ربيع الثاني",
        "جمادى الأولى", "جمادى الآخرة", "رجب", "شعبان",
        "رمضان", "شوال", "ذو القعدة", "ذو الحجة"
    ]
    
    # Extract day, month, and year from the Hijri date
    hijri_day = number_to_arabic(hijri_date.day)
    hijri_month = arabic_months[hijri_date.month - 1]  # Adjust index to match array
    hijri_year = number_to_arabic(hijri_date.year)
    
    # Return the formatted output
    return f"اليوم هو {hijri_day} من {hijri_month} سنة {hijri_year}"

