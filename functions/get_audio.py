import speech_recognition as sr

def get_audio(lang='ar'):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("قل شيئًا!")  # "Say something!" in Arabic
        audio = r.listen(source) 
    try:
        text = r.recognize_google(audio, language=lang)
        print("لقد قلت: " + text)  # "You said: " in Arabic
        return text
    except sr.UnknownValueError:
        print("لم أفهم ما قلت")  # "Google Speech Recognition could not understand audio" in Arabic
        return ""
    except sr.RequestError as e:
        print(f"لا يمكن طلب النتائج من خدمة التعرف على الكلام من Google؛ {e}")  # "Could not request results from Google Speech Recognition service; {e}" in Arabic
        return ""
