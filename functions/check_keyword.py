from functions.time import get_time
from functions.date_meladi import get_gregorian_date
from functions.date_Hijri import get_hijri_date
from functions.light_condition import check_light_condition
from functions.currency import detect_currency


def check_keyword(keyword):
    if keyword == "معرفة-الوقت":
        print(get_time())
    elif keyword == "معرفة-التاريخ":
        print(get_gregorian_date())
        print(get_hijri_date())
    elif keyword == "فحص-الإضاءة":
        check_light_condition()
    elif keyword == "كشف-العملة":
        if check_light_condition == ():
            print(detect_currency()) 
        else:
            break  
    else:
        print("الكلمة الرئيسية غير صحيحة.")
