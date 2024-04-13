from functions.time import get_time
from functions.date_meladi import get_gregorian_date
from functions.date_Hijri import get_hijri_date
from functions.light_condition import check_light_condition
from functions.currency import detect_currency
from functions.snapshot import snapshot


def check_keyword(keyword):
    if keyword == "معرفة-الوقت":
        print(get_time())
    elif keyword == "معرفة-التاريخ":
        print(get_gregorian_date())
        print(get_hijri_date())
    elif keyword == "فحص-الإضاءة":
        check_light_condition()
    elif keyword == "كشف-العملة":
        light_condition = check_light_condition()
        if light_condition == "الإضاءة كافية":
            print(detect_currency(snapshot()))
        else:
            print("الإضاءة غير كافية")

    else:
        print("الكلمة الرئيسية غير صحيحة.")
