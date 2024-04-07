from functions.get_audio import get_audio
from functions.gemini import get_keyword_for_query
from functions.time import get_time

captured_voice = get_audio()

response_keyword = get_keyword_for_query(captured_voice)
print(response_keyword)

def check_keyword(keyword):
    if keyword == "معرفة-الوقت":
        print(get_time())
    else:
        print("الكلمة الرئيسية غير صحيحة.")

