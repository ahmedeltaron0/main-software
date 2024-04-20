import google.generativeai as genai
import os
from deep_translator import GoogleTranslator
from PIL import Image
from dotenv import dotenv_values

GEMINI_KEY = dotenv_values('.env').get('gemini_api')

genai.configure(api_key=os.getenv("AIzaSyBWGO_ggtKGhgTwrHV61ubrNMomEyk5wdc") or "AIzaSyBWGO_ggtKGhgTwrHV61ubrNMomEyk5wdc")

model =  genai.GenerativeModel("gemini-pro")
vision_model = genai.GenerativeModel("models/gemini-pro-vision")

def gemini_response(query):
    en_translated_query = GoogleTranslator(source='auto', target='en').translate(query)

    response = model.generate_content("Answery briefly, \n" + en_translated_query).text

    ar_translated_rsponse = GoogleTranslator(source='auto', target='ar').translate(response.text)

    return ar_translated_rsponse


def detect_currency(img, question = 'How much money is in this image ?'):
    # response = vision_model.generate_content(Image.fromarray(img))  # simply pass the image
    # print(response.text)
    # #Output:
    # # Stunning!
    en_translated_query = GoogleTranslator(source='auto', target='en').translate(question)


    response = vision_model.generate_content([en_translated_query, Image.fromarray(img)])  
    
    ar_translated_rsponse = GoogleTranslator(source='auto', target='ar').translate(response.text)

    # pass image and text
    print(ar_translated_rsponse)
    
    return ar_translated_rsponse

